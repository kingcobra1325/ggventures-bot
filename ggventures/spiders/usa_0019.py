import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Usa0019Spider(scrapy.Spider):
    name = 'usa_0019'
    country = 'US'
    start_urls = ["https://www8.gsb.columbia.edu/calendar"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            # event_name = list()
            # event_date = list()
            # event_time = list()
            # event_desc = list()
            # event_link = list()

            self.driver.get("https://home.gsb.columbia.edu/")

            logo = 'https://yt3.ggpht.com/ytc/AKedOLRfHXTUpy0athnHliRsncdRBUkvMlw1SsBdzTdljg=s900-c-k-c0x00ffffff-no-rj'

            university_name = self.driver.find_element(By.XPATH , "//title").get_attribute('textContent')

            self.driver.get("https://mason.wm.edu/contact/index.php")

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//table[contains(@summary,'Contact Table')]//tr")))).text

            self.driver.get(response.url)

            select = Select(WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'jump_menu')]"))))
            select.select_by_value('all')

            time.sleep(4)

            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@title,'Expand to View')]")))

            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                if 'gsb.columbia.edu' in i.get_attribute('href'):

                    data = ItemLoader(item = GgventuresItem(), selector = i)
                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    data.add_value('event_name', WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH, "//h1"))).text)
                    data.add_value('event_desc', self.getter.find_elements(By.XPATH , "//div[contains(@class,'col-md-4_5')]//p")[0].text)
                    data.add_value('event_date', self.getter.find_elements(By.XPATH , "//div[contains(@class,'col-md-4_5')]//p")[1].text)
                    data.add_value('event_time', self.getter.find_element(By.XPATH , "//div[contains(@id,'event_details')]").text)
                    data.add_value('event_link', i.get_attribute('href'))

                    yield data.load_item()
                else:
                    logger.debug(f"Link: {i.get_attribute('href')} is located outside the Website. Skipping.....")


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
