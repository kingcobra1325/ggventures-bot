import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, website_changed

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0031Spider(scrapy.Spider):
    name = 'usa_0031'
    country = 'US'
    start_urls = ["https://www.georgetown.edu/events/calendar/MSB/"]

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

            self.driver.get("https://msb.georgetown.edu/")
            
            logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@alt,'McDonough School of Business logo')]")))).get_attribute('src')
            
            university_name = self.driver.find_element(By.XPATH , "//title").get_attribute('textContent')
            
            self.driver.get("https://msb.georgetown.edu/about/paul-almeida/contact-dean/")
  
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.XPATH,"//h2[text()='Contact Information']/following-sibling::p")))).text
            
            self.driver.get(response.url)
            
            no_events = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(text(),'no upcoming events')]")))
            # no_events = self.driver.find_element(By.XPATH, "//li[contains(text(),'No upcoming')]")

            if not no_events:
                logger.debug('Changes to Events on current Spider. Sending emails....')
                website_changed(self.name,university_name)
            else:
                logger.debug('No changes to Events on current Spider. Skipping.....')
            
            
            
                       
            
            # for i in range(3):
            #     EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'fc-event')]/a")))
                
            #     for i in EventLinks:
            #         self.getter.get(i.get_attribute('href'))
                        
            #         RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='title']")))).text
                    
            #         RawEventDesc = self.getter.find_element(By.XPATH,"//div[@class='desc']").text

            #         RawEventDate = self.getter.find_element(By.XPATH,"//div[@class='row'][2]").text + self.getter.find_element(By.XPATH,"//div[@class='row'][3]").text
                    
            #         try:
            #             RawEventTime = self.getter.find_element(By.XPATH,"//div[@class='row'][2]").text + self.getter.find_element(By.XPATH,"//div[@class='row'][3]").text
            #         except:
            #             RawEventTime = None

                        
            #         event_name.append(RawEventName)
            #         event_desc.append(RawEventDesc)
            #         event_date.append(RawEventDate)
            #         event_time.append(RawEventTime)
            #         event_link.append(i.get_attribute('href'))     
                
            #     Nextbutton = self.driver.find_element(By.XPATH,"//div[contains(@class,'fc-button-next')]/a").click()
                  
            

            # for i in range(len(event_name)):
            #     data = ItemLoader(item = GgventuresItem(), selector = i)
            #     data.add_value('university_name',university_name)
            #     data.add_value('university_contact_info',university_contact_info)
            #     data.add_value('logo',logo)
            #     data.add_value('event_name', event_name[i])
            #     data.add_value('event_desc', event_desc[i])
            #     data.add_value('event_date', event_date[i])
            #     data.add_value('event_time', event_time[i])
            #     data.add_value('event_link', event_link[i])
                
            #     yield data.load_item()
            
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
