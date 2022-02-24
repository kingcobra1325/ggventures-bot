import scrapy, time

from datetime import datetime

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller, EventBrite_API

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# def counter(function):
#     """
#     Wraps function with a Try-Except Catch
#     """
#     def wrapper(*args,**kwargs):
#         try:
#             function(*args,**kwargs)
#         except Exception as e:
#             logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
#             error_email(self.name,e)
#     return wrapper


class Aus0019Spider(GGVenturesSpider):
    name = 'aus_0019'
    start_urls = ['https://cbe.anu.edu.au/welcome-cbe/']
    country = 'Australia'
    eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    # static_name = ''
    static_logo = 'https://cbe.anu.edu.au/sites/default/files/2x_anu_logo_small_over.png'

    parse_code_link = 'https://cbe.anu.edu.au/events'

    def get_university_contact_info(self,response):
        self.driver.get(response.url)
        self.university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//section[contains(@id,'contactdetails')]")))).text

    def parse_code(self,response):
        self.driver.get(response.url)
        EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'news-right')]/h3/a")))

        for i in EventLinks:

            data = ItemLoader(item = GgventuresItem(), selector = i)

            link = i.get_attribute('href')
            self.getter.get(link)

            if self.unique_event_checker(url_substring='anu.edu.au/events'):

                logger.info(f"Currently scraping --> {self.getter.current_url}")

                item_data = self.item_data_empty.copy()

                item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                try:
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-left-col')]").text
                except NoSuchElementException as e:
                    logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text


                try:
                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-right-col')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-right-col')]").text
                except NoSuchElementException as e:
                    logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text

                item_data['startups_contact_info'] = ''
                item_data['event_link'] = link

                loaded_item = self.load_item(item_data=item_data,item_selector=i)

                logger.info(f"THIS IS THE LOADED ITEM --> {loaded_item}")

                yield loaded_item
