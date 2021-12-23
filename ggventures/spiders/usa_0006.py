import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

class Usa0006Spider(scrapy.Spider):
    name = 'usa-0006'
    country = 'US'
    start_urls = ['https://www.baylor.edu/business/news/index.php?id=86163']
    
    def __init__(self):
        self.driver = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get(response.url)
            
            event_name = list()
            event_date = list()
            event_time = list()
            event_desc = list()

            logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class ,'logo')]")))).value_of_css_property('background')
            logo = re.findall(r'''\"(\S+)\"''',logo)[0]
            
            university_name = self.driver.find_element(By.XPATH , "//a[contains(@class,'logo')]").get_attribute('textContent')

            university_contact_info = self.driver.find_element(By.XPATH,"//div[contains(@id, 'copyright')]/p").text.split('\n')[1]

            Next_Link = self.driver.find_element(By.XPATH, "//input[contains(@type, 'submit')]")
            Next_Link.click()
                
            for i in range(2):
                EventLinks = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'notResponsive')]//td[contains(@align, 'left')]/a")
                for i in EventLinks:
                    i.click()
                    print(len(self.driver.window_handles))
                    new_window = self.driver.window_handles[1]
                    self.driver.switch_to.window(new_window)
                    event_name.append((WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@id, 'content')]/h1")))).text)
                    eventDescCount = self.driver.find_elements(By.XPATH,"//tbody/tr")
                    if len(eventDescCount) <= 3:
                        event_desc.append(None)
                    elif len(eventDescCount) == 4:
                        event_desc.append(self.driver.find_element(By.XPATH, "//tr[2]").text)
                    elif len(eventDescCount) >= 5:
                        event_desc.append(self.driver.find_element(By.XPATH, "//tr[3]").text)
                    else:
                        event_desc.append(None)
                    event_date.append(self.driver.find_element(By.XPATH, "//tr[1]/td[2]").text)
                    try:
                        event_time.append(self.driver.find_element(By.XPATH, "//tr[1]/td[4]").text)
                    except:
                        event_time.append('All Day')
                    #Some events don't have time and element position changes depends on the event
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.get(self.driver.find_element(By.XPATH,"//div[contains(@class, 'box_title')]/a[3]").get_attribute('href'))
                
            for i in range(len(event_name)):
                data = ItemLoader(item = GgventuresItem(), selector = i)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                data.add_value('logo',logo)
                data.add_value('event_name', event_name[i])
                data.add_value('event_desc', event_desc[i])
                data.add_value('event_date', event_date[i])
                data.add_value('event_time', event_time[i])
                yield data.load_item()
        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
        
    def closed(self, reason):
        try:
            self.driver.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
