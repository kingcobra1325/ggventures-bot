import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0014Spider(scrapy.Spider):
    name = 'usa_0014'
    country = 'US'
    start_urls = ['https://www.cmu.edu/tepper/news/events/index.html']

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

            height = self.driver.execute_script("return document.body.scrollHeight")

            self.driver.get("https://www.cmu.edu/tepper/")

            logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@alt,'Tepper School')]")))).get_attribute('href')

            university_name = self.driver.find_element(By.XPATH , "//title").get_attribute('textContent')

            self.driver.get("https://www.cmu.edu/tepper/contact-us.html")

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'grid column2  grey  boxes  js-list')]/div/p[1]")))).text

            self.driver.get(response.url)

            WebScroller(self.driver,height)

            self.driver.switch_to.frame(WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//iframe[@title='calendar']"))))

            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(@class,'ng-scope')]/a")))


            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//span[contains(@ng-bind-html,'event.content.summary.text')]")))).text

                RawEventDesc = self.getter.find_element(By.XPATH,"//div[contains(@ng-bind-html,'fe.safeDesc')]").text

                RawEventDate = self.getter.find_element(By.XPATH,"//div[contains(@class,'d-when eventDetail__when')]").text

                try:
                    RawEventTime = self.getter.find_element(By.XPATH,"//div[contains(@class,'d-when eventDetail__when')]").text
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
