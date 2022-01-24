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

class Usa0142Spider(scrapy.Spider):
    name = 'usa_0142'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://foster.uw.edu/news-events/trumba/"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://foster.uw.edu/")

            logo = "https://www.kindpng.com/picc/m/677-6776504_university-of-washington-foster-school-of-business-uw.png"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Washington,Business School"
            
            self.driver.get("https://foster.uw.edu/contacts/")
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//tbody")))).text

            self.driver.get(response.url)     
            
            counter = 0
            for o in range(3):
                EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@role='heading']/a")))
                for i in EventLinks:
                    self.getter.get(i.get_attribute('href'))

                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='twEDDescription']")))).text

                    try:
                        RawEventDesc = self.getter.find_element(By.XPATH,"//span[text()='Description']/../following-sibling::td").text
                    except:
                        RawEventDesc = None

                    RawEventDate = self.getter.find_element(By.XPATH,"//span[text()='When']/../following-sibling::td").text 

                    try:
                        RawEventTime = RawEventDate
                    except:
                        RawEventTime = None
                        
                    # try:
                    #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//dt[@class='custom-field-contact']/..").text
                    # except:
                    #     RawStartContactInfo = None
                        
                    try:
                        RawStartUpLink = self.getter.find_element(By.XPATH,"//span[text()='Online Meeting Link']/../following-sibling::td").text
                    except:
                        RawStartUpLink = None

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
                    data.add_value('startups_link', RawStartUpLink)
                    counter+=1

                    yield data.load_item()
            self.driver.get(self.driver.find_element(By.XPATH,"//a[@title='Next Page']").get_attribute('href'))

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