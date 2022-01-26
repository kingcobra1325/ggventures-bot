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

class Usa0148Spider(scrapy.Spider):
    name = 'usa_0148'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://business.wfu.edu/events/"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://business.wfu.edu/")

            logo = "https://business.wfu.edu/wp-content/themes/WFU-Business/images/logo-reg.png"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "Wake Forest University,Babcock Graduate School of Management"
            
            self.driver.get("https://business.wfu.edu/contact-us/")
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"(//li[@class='active'])[2]/../..")))).text

            self.driver.get(response.url)     
            
            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='fc-title']/../..")))
            for i in EventLinks:
                i.click()
                self.driver.switch_to_window(self.driver.window_handles[1])

                RawEventName = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//h1")))).text

                try:
                    RawEventDesc = self.driver.find_element(By.XPATH,"//div[@class='description']").text
                except:
                    RawEventDesc = None

                RawEventDate = self.driver.find_element(By.XPATH,"//p[@class='dateright']").text 

                try:
                    RawEventTime = RawEventDate
                except:
                    RawEventTime = None
                    
                try:
                    RawStartContactInfo = self.driver.find_element(By.XPATH,"//dt[@class='custom-field-contact_phone_number']/..").text
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
                data.add_value('event_link', self.driver.current_url)
                data.add_value('startups_contact_info', RawStartContactInfo)
                counter+=1

                yield data.load_item()
                self.driver.close()
                self.driver.switch_to_window(self.driver.window_handles[0])

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