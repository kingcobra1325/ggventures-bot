import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0059Spider(scrapy.Spider):
    name = 'usa_0059'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://business.rice.edu/events"]

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

            self.driver.get("https://business.rice.edu/")

            logo = "https://business.rice.edu/sites/default/files/Rice-I-Business-logo-w-tag-full-final_JGSB.jpg"

            university_name = "RRice University,Jesse H. Jones Graduate School of Management"
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'footer-contact')]//div[@class='f--field f--wysiwyg']")))).text

            self.driver.get(response.url)

            for o in range(2):
                self.driver.find_element(By.XPATH,"//a[@rel='next']").click()
                
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div/following-sibling::div[@class='ally-focus-within']//section[contains(@class,'events-listing')]//h3//a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'section-title')]/h2")))).text

                try:
                    RawEventDesc = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//section[@aria-label='Body text']")))).text
                except:
                    RawEventDesc = None

                RawEventDate = None

                try:
                    RawEventTime = RawEventDate
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
