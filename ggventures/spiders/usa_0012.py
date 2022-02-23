import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, website_changed

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0012Spider(scrapy.Spider):
    name = 'usa_0012'
    country = 'US'
    start_urls = ['https://www.csuchico.edu/contact/index.shtml']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get(response.url)

            logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class,'csuc-signature')]/img")))).get_attribute('src')

            university_name = self.driver.find_element(By.XPATH , "//a[contains(@class,'csuc-signature')]/img").get_attribute('alt')

            university_contact_info = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Information Center')]/following-sibling::ul").text

            self.driver.get("https://www.csuchico.edu/cob/events/index.shtml")

            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='title']")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                try:
                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='page-title']")))).text
                except:
                    RawEventName = None

                try:
                    RawEventDesc = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'primary-content')]").text
                except:
                    RawEventDesc = None

                try:
                    RawEventDate = self.getter.find_element(By.XPATH,"//strong[@class='announcement-date']").text
                except:
                    RawEventDate = None

                try:
                    RawEventTime = RawEventDate
                except:
                    RawEventTime = None

                try:
                    RawStartContactInfo = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'primary-content')]//p//br/..").text
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
