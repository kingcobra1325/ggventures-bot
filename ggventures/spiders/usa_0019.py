import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Usa0019Spider(scrapy.Spider):
    name = 'usa_0019'
    country = 'US'
    start_urls = ["https://www8.gsb.columbia.edu/calendar"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            logo = 'https://yt3.ggpht.com/ytc/AKedOLRfHXTUpy0athnHliRsncdRBUkvMlw1SsBdzTdljg=s900-c-k-c0x00ffffff-no-rj'

            university_name = "Columbia University,Columbia Business School (CBS)"

            self.driver.get("https://www8.gsb.columbia.edu/contact")

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='copyright']")))).text

            self.driver.get(response.url)

            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='eventolink']/a")))


            counter = 0
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                if "https://groups.gsb.columbia.edu/" in self.getter.current_url:
                    
                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='rsvp__event-name']")))).text

                    try:
                        RawEventDesc = self.getter.find_element(By.XPATH,"//div[@id='event_details']").text
                    except:
                        RawEventDesc = None

                    try:
                        RawEventDate = self.getter.find_element(By.XPATH,"//span[@id='timezone']/../..").text 
                    except:
                        RawEventDate = None
                        
                    try:
                        RawEventTime = RawEventDate                  
                        # RawEventTime = self.getter.find_element(By.XPATH,"//p[@Class='event__time']").text 
                        # RawEventTime = RawEventDate
                    except:
                        RawEventTime = None
                        
                    # try:
                    #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//section[contains(@class,'contact')]").text
                    # except:
                    #     RawStartContactInfo = None

                    data = ItemLoader(item = GgventuresItem(), selector = i)
                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    data.add_value('event_name', RawEventName)
                    data.add_value('event_desc', RawEventDesc)
                    data.add_value('event_date', RawEventDate)
                    data.add_value('event_time', RawEventTime)
                    data.add_value('event_link', i.get_attribute('href'))

                    counter+=1
                    yield data.load_item()
                else:
                    logger.debug(f"Link: {i.get_attribute('href')} is a Unique Event. Sending Emails.....")
                    unique_event(self.name,university_name,i.get_attribute('href'))
                    logger.debug("Skipping............")


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
