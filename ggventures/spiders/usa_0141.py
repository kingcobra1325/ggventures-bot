import scrapy
import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0141Spider(scrapy.Spider):
    name = 'usa_0141'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://www.darden.virginia.edu/events"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://www.darden.virginia.edu/")

            logo = "https://www.darden.virginia.edu/themes/custom/darden_main/images/logo.svg"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Virginia,Darden School of Business"
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'address')]")))).text

            self.driver.get(response.url)     
            
            counter = 0
            
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='node__content']/a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                
                if 'https://apply.darden.virginia.edu/' in self.getter.current_url:
                    EventNameXPATH = "//h1"
                    EventDescXPATH = "//div[@id='form_description']"
                    EventDateXPATH = "//p[@id='register_date']"
                    EventStartContactXPATH = ""
                elif 'https://darden.imodules.com/' in self.getter.current_url:
                    EventNameXPATH = "//h1"
                    EventDescXPATH = "//div[@class='imod_eventDescription']"
                    EventDateXPATH = "//div[@class='imod_eventDate']"
                    EventStartContactXPATH = "//div[@class='imod_eventContactPrimary']"
                else:
                    logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                    unique_event(self.name,university_name,self.getter.current_url)
                    logger.debug("Skipping............")

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,EventNameXPATH)))).text

                try:
                    RawEventDesc = self.getter.find_element(By.XPATH,EventDescXPATH).text
                except:
                    RawEventDesc = None

                RawEventDate = self.getter.find_element(By.XPATH,EventDateXPATH).text 

                try:
                    RawEventTime = RawEventDate
                except:
                    RawEventTime = None
                    
                try:
                    RawStartContactInfo = self.getter.find_element(By.XPATH,EventStartContactXPATH).text
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