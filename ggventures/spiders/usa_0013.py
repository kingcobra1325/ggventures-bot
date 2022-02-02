import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, Load_FF_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Usa0013Spider(scrapy.Spider):
    name = 'usa_0013'
    country = 'US'
    start_urls = ['https://www.csulb.edu/']

    def __init__(self):
        self.driver = Load_Driver()
        # self.driver = Load_FF_Driver()
        self.getter = Load_Driver()
        # self.getter = Load_FF_Driver()
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
            logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Long_Beach_State_Athletics_logo.svg/1200px-Long_Beach_State_Athletics_logo.svg.png"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "California State University - Long Beach"

            university_contact_info = self.driver.find_element(By.XPATH, "//div[@class='vcard']").text

            # self.driver.get(response.url)

            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='block-bean-homepage-events']//div[@class='field-items']//a")))

            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

            try:
                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h2[@itemprop='summary']")))).text
            except:
                RawEventName = None
                
            try:
                RawEventDesc = self.getter.find_element(By.XPATH,"//div[@id='eventDescriptionEventDetails']").text
            except:
                RawEventDesc = None

            try:
                RawEventDate = self.getter.find_element(By.XPATH,"//div[@class='info-date']").text 
            except:
                RawEventDate = None
                
            try:
                RawEventTime = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'info-time')]").text 
            except:
                RawEventTime = None
                
            # try:
            #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'primary-content')]//p//br/..").text
            # except:
            #     RawStartContactInfo = None

            data = ItemLoader(item = GgventuresItem(), selector = counter)
            data.add_value('university_name',university_name)
            data.add_value('university_contact_info',university_contact_info)
            data.add_value('logo',logo)
            data.add_value('event_name', RawEventName)
            data.add_value('event_desc', RawEventDesc)
            data.add_value('event_date', RawEventDate)
            data.add_value('event_time', RawEventTime)
            data.add_value('event_link', i.get_attribute('href'))
            # data.add_value('startups_contact_info', RawStartContactInfo)
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
