import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Usa0011Spider(scrapy.Spider):
    name = 'usa_0011'
    country = 'US'
    start_urls = ['https://marriott.byu.edu/']
    # start_urls = ['https://marriott.byu.edu/calendar/?id=events']

    def __init__(self):
        self.driver = Load_Driver()
        # self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get(response.url)
            #cannot find logo in website but it appears in fb
            logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//img[@id='full-logo']")))).get_attribute('src')
            university_name = self.driver.find_element(By.XPATH , "//title").get_attribute('textContent')
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]
            self.driver.get('https://marriott.byu.edu/contact/')

            contact_name = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'EMBA')]"))).text

            contact_details = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'EMBA')]/following-sibling::p"))).text

            university_contact_info = f"{contact_name} \n {contact_details}"

            self.driver.get("https://marriott.byu.edu/calendar/?id=events")

            self.driver.switch_to.frame(WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@class,'calendar')]"))))

            # Iframe_Container = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@id,'eventContainer1')]")))
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@id,'eventContainer1')]")))

            C2L = self.driver.find_elements(By.XPATH, ".//div[contains(@class,'day')]")

            for i in C2L:
                i.click()

            # EventLinks = Iframe_Container.find_elements(By.XPATH, ".//div[contains(@class,'day')]")
            EventLinks = self.driver.find_elements(By.XPATH, ".//div[contains(@class,'day')]")

            for i in EventLinks:
                try:
                    # self.getter.get(i.get_attribute('href'))
                    data = ItemLoader(item = GgventuresItem(), selector = i)

                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    event_summary = i.find_element(By.XPATH, ".//div[contains(@class,'event-summary')]")
                    data.add_value('event_name', event_summary.text)
                    # data.add_value('event_desc', event_desc[i])
                    data.add_value('event_date', i.find_element(By.XPATH, ".//div[contains(@class,'date-label')]").text)
                    # data.add_value('event_time', event_time[i])
                    # event_summary.click()
                    data.add_value('event_link', i.find_element(By.XPATH, ".//div[contains(@class,'event-links')]/a").get_attribute('href'))
                    yield data.load_item()
                except NoSuchElementException as e:
                    logger.error(f"Unable to parse information ---> {e}")


        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)

    def closed(self, reason):
        try:
            self.driver.quit()
            # self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
