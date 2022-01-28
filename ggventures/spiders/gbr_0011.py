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

class Gbr0011Spider(scrapy.Spider):
    name = 'gbr_0011'
    country = 'United Kingdom'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://www.henley.ac.uk/events/upcoming"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://www.henley.ac.uk/")

            logo = "https://i2.wp.com/www.henleymba9091.com/wp-content/uploads/2018/02/Henley-Business-School-Transparent-Logo.png?ssl=1"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "Henley Management College"
            
            self.driver.get("https://www.henley.ac.uk/about/find-us")
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='container']")))).text

            self.driver.get(response.url)     
            
            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='w-full']//h3/a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1")))).text

                try:
                    RawEventDesc = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'pretty')]").text
                except:
                    RawEventDesc = None

                RawEventDate = self.getter.find_element(By.XPATH,"//th[contains(text(),'Date')]/..").text 

                try:
                    RawEventTime = self.getter.find_element(By.XPATH,"//th[contains(text(),'Time')]/..").text 
                except:
                    RawEventTime = None
                    
                try:
                    RawStartContactInfo = self.getter.find_element(By.XPATH,"//h2[text()='Contact us']/..").text
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