import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0026Spider(scrapy.Spider):
    name = 'usa_0026'
    country = 'US'
    start_urls = ["https://goizueta.emory.edu/events"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.getter2 = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None
        
    def parse(self, response):
        try:
            event_name = list()
            event_date = list()
            event_time = list()
            event_desc = list()
            event_link = list()

            self.driver.get("https://goizueta.emory.edu/")
            
            #svg
            # logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class,'logo-long d-none d-md-block')]")))).value_of_css_property('background-image')
            
            university_name = self.driver.find_element(By.XPATH , "//div[contains(@class,'site-logo')]//*[local-name() = 'svg']//*[local-name() ='title']").get_attribute('textContent')
  
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'contact__phone')]")))).text
            
            self.driver.get(response.url)    
            
            NextLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'pager__page-link')]")))
            for o in NextLinks:
                self.getter.get(o.get_attribute('href'))
                EventLinks = WebDriverWait(self.getter,60).until(EC.presence_of_all_elements_located((By.XPATH,"//h3[contains(@class,'heading event-card__title')]/a")))
                
                for i in EventLinks:
                    self.getter2.get(i.get_attribute('href'))
                        
                    RawEventName = (WebDriverWait(self.getter2,60).until(EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'heading__light')]")))).text
                    
                    RawEventDesc = self.getter2.find_element(By.XPATH,"//div[contains(@class,'event-section event__details')]").text
    
                    RawEventDate = self.getter2.find_element(By.XPATH,"//div[contains(@class,'event-card__date--inner')]").text
                    
                    try:
                        RawEventTime = self.getter2.find_element(By.XPATH,"//div[contains(@class,'event__label--wrapper')]/span[2]").text
                    except:
                        RawEventTime = None

                        
                    event_name.append(RawEventName)
                    event_desc.append(RawEventDesc)
                    event_date.append(RawEventDate)
                    event_time.append(RawEventTime)
                    event_link.append(i.get_attribute('href'))        
                

            for i in range(len(event_name)):
                data = ItemLoader(item = GgventuresItem(), selector = i)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                # data.add_value('logo',logo)
                data.add_value('event_name', event_name[i])
                data.add_value('event_desc', event_desc[i])
                data.add_value('event_date', event_date[i])
                data.add_value('event_time', event_time[i])
                data.add_value('event_link', event_link[i])
                
                yield data.load_item()
            
        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)    
    def closed(self, reason):
        try:
            self.driver.quit()
            self.getter.quit()
            self.getter2.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
