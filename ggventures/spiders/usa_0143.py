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

class Usa0143Spider(scrapy.Spider):
    name = 'usa_0143'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://business.wisc.edu/events/"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://business.wisc.edu/")

            logo = "https://business.wisc.edu/wp-content/uploads/2021/10/WSB_Web_Horizontal_UW-Madison.svg"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Wisconsin - Madison,School of Business"
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='address']")))).text

            self.driver.get(response.url)     
            
            counter = 0
            for o in range(2):
                EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//h3/a")))
                for i in EventLinks:
                    self.getter.get(i.get_attribute('href'))

                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1")))).text

                    try:
                        RawEventDesc = self.getter.find_element(By.XPATH,"//div[@class='tribe-events-schedule tribe-clearfix']/following-sibling::p").text
                    except:
                        RawEventDesc = None

                    RawEventDate = self.getter.find_element(By.XPATH,"//div[@class='tribe-events-schedule tribe-clearfix']").text 

                    try:
                        RawEventTime = RawEventDate
                    except:
                        RawEventTime = None
                        
                    try:
                        RawStartContactInfo = self.getter.find_element(By.XPATH,"//div[contains(@class,'organizer')]").text
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
                self.driver.get(self.driver.find_element(By.XPATH,"//a[@rel='next']").get_attribute('href'))
            

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