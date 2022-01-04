import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0032Spider(scrapy.Spider):
    name = 'usa_0032'
    country = 'US'
    start_urls = ["https://www.scheller.gatech.edu/news-events/events/index.html"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None
        
    def parse(self, response):
        try:
            event_name = list()
            event_date = list()
            event_time = list()
            event_desc = list()
            event_link = list()

            self.driver.get("https://www.scheller.gatech.edu/index.html")
            
            logo = 'https://i.pinimg.com/736x/fa/11/55/fa11556b78f9e814d32191cac1ab5d81--atlanta-georgia-partner.jpg'
            
            university_name = self.driver.find_element(By.XPATH , "//address//strong").text
  
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.XPATH,"//address")))).text
            
            self.driver.get(response.url)           
            
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//li[@class='featured event' or @class='event']/a")))
            
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                    
                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[@id='main']/h1")))).text

                RawEventDesc = self.getter.find_element(By.XPATH,"//div[@class='signup']//div[contains(@class,'clearfix')][1]").text + "\n" + self.getter.find_element(By.XPATH,"//div[@class='signup']//div[contains(@class,'clearfix')][2]").text

                RawEventDate = self.getter.find_element(By.XPATH,"//div[@class='event-content']//div[@class='grid_6 alpha']/h4").text
                
                try:
                    RawEventTime = self.getter.find_element(By.XPATH,"//time[@itemprop='startDate']").text + '-' +self.getter.find_element(By.XPATH,"//time[@itemprop='endDate']").text
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
                data.add_value('logo',logo)
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
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
