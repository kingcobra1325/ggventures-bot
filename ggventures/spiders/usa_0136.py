import scrapy
import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0136Spider(scrapy.Spider):
    name = 'usa_0136'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://www.marshall.usc.edu/news-events/usc-marshall-events"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://www.marshall.usc.edu/")

            logo = "https://upload.wikimedia.org/wikipedia/commons/f/ff/USC_Marshall_logo.png"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Southern California (USC),Marshall School of Business"
            
            self.driver.get("https://www.marshall.usc.edu/about/contact-us")
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='table-wrap']")))).text

            self.driver.get(response.url)     
            
            height = self.driver.execute_script("return document.body.scrollHeight")
            
            WebScroller(self.driver,height)
            
            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//h4/a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                
                if 'https://ticketbud.com/' in self.getter.current_url:
                    RawEventNameXPATH = "//h1"
                    RawEventDescXPATH = "//div[@id='event-details']"
                    RawEventDateXPATH = "//div[@class='date-and-time-details']"
                elif 'https://www.marshall.usc.edu/event/' in self.getter.current_url:
                    RawEventNameXPATH = "//h2[@class='block-story__title']"
                    RawEventDescXPATH = "//div[contains(@class,'text-content')]"
                    RawEventDateXPATH = "//div[@class='block-story__body']"
                    

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,RawEventNameXPATH)))).text

                try:
                    RawEventDesc = self.getter.find_element(By.XPATH,RawEventDesc).text
                except:
                    RawEventDesc = None

                RawEventDate = self.getter.find_element(By.XPATH,RawEventDateXPATH).text 

                try:
                    RawEventTime = RawEventDate
                except:
                    RawEventTime = None
                    
                try:
                    RawStartContactInfo = None
                except:
                    RawStartContactInfo = None

                data = ItemLoader(item = GgventuresItem(), selector = counter)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                data.add_value('logo',logo)
                data.add_value('event_name', RawEventName)
                data.add_value('event_desc', RawEventDesc)
                data.add_value('event_date', RawEventDate)
                data.add_value('event_time', RawEventTime)
                data.add_value('event_link', i.get_attribute('href'))
                data.add_value('startups_contact_info', RawStartContactInfo)
                counter+=1

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