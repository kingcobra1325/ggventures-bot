import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0010Spider(scrapy.Spider):
    name = 'usa-0010'
    country = 'US'
    start_urls = ['https://www.bradley.edu/academic/colleges/fcba/']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None
        
    def parse(self, response):
        try:
            self.driver.get(response.url)
            
            event_name = list()
            event_date = list()
            event_time = list()
            event_desc = list()

            #cannot find logo in website but it appears in fb
            # logo = (WebDriv   erWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'brand')]/a")))).value_of_css_property('background')
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]
            
            university_name = self.driver.find_element(By.XPATH , "//title").get_attribute('textContent')
            
            university_contact_info = self.driver.find_element(By.XPATH, "//div[contains(@class,'row row-padding-sm')]//div[contains(@class,'col-md-8')]").get_attribute('textContent')
            
            self.driver.get("https://www.bradley.edu/calendar/")

            EventLinks = self.driver.find_elements(By.XPATH, "//h3/a")
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                    
                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'col-md-5')]//a")))).text
                
                RawEventDesc = self.getter.find_element(By.XPATH,"//div[contains(@class,'col-md-7')]").text
                
                RawEventDate = self.getter.find_element(By.XPATH,"//div[contains(@class,'col-md-5')]/p[2]").text
                
                try:
                    RawEventTime = self.getter.find_element(By.XPATH,"//div[contains(@class,'col-md-5')]//p[3]").text
                except:
                    RawEventTime = None

                    
                event_name.append(RawEventName)
                event_desc.append(RawEventDesc)
                event_date.append(RawEventDate)
                event_time.append(RawEventTime)

            for i in range(len(event_name)):
                data = ItemLoader(item = GgventuresItem(), selector = i)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                # data.add_value('logo',logo)
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
            self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)