import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0001Spider(scrapy.Spider):
    name = 'usa_0001'
    country = 'US'
    start_urls = ['https://kogod.american.edu/events?hsLang=en']

    def __init__(self):
        self.driver = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get(response.url)
            height = self.driver.execute_script("return document.body.scrollHeight")

            WebScroller(self.driver,height)

            university_name = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'header__main')]/a")))).text
            university_contact_info = self.driver.find_element(By.XPATH,"//div[contains(@class, 'hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module')]/ul[contains(@class, 'footer__list')]").text

            # logo = (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@alt, 'American University Homepage')]")))).get_attribute('src')

            RawEventName = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'events__title')]")))
            RawEventDesc = self.driver.find_elements(By.XPATH,"//div[contains(@class, 'event__content')]/p")
            RawEventDate = self.driver.find_elements(By.XPATH,"//article//div[contains(@class, 'events-carousel__date')]")
            RawEventTime = self.driver.find_elements(By.XPATH,"//div[contains(@class,'events-carousel__time')]")

            for i in range(len(RawEventName)):
                data = ItemLoader(item = GgventuresItem(), selector = i)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                # data.add_value('logo',logo)
                # data.add_value('event_time',event_time)
                # data.add_value('event_link',event_link)
                # data.add_value('startups_name',startups_name)
                # data.add_value('startups_link',startups_link)
                # data.add_value('startups_contact_info',startups_contact_info)
                data.add_value('event_name', RawEventName[i].text)
                data.add_value('event_desc', RawEventDesc[i].text)
                data.add_value('event_date', RawEventDate[i].text.replace('\n',' '))
                data.add_value('event_time', RawEventTime[i].get_attribute('textContent').strip())
                yield data.load_item()
        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
            # logger.info(f"Fetching Event Date: {RawEventDate[i].text.replace('\n',' ')}")

    def closed(self, reason):
        try:
            self.driver.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)


        # raw_page = Selector(text=response.page_source)
        # data = GgventuresItem()
        # data['event_name'] = response.xpath("//div[contains(@class, 'events__title')]")
        # logger.info(f"Fetching Event Name: {data['event_name']}")
