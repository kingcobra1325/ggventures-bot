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


class Usa0036Spider(GGVenturesSpider):
    name = 'usa_0036'
    country = 'US'
    start_urls = ["https://www2.howard.edu/contact"]
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'Howard University,School of Business'
    static_logo = 'https://economist-findercms-files.s3.us-west-1.amazonaws.com/2018-10/howardlg01.jpg'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://calendar.howard.edu/'

    university_contact_info_xpath = "//div[contains(@class,'contact_info')]"
    contact_info_text = True
    # contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//p[text()='No upcoming events.']")

            # for link in self.multi_event_pages(self,num_of_pages=6,event_links_xpath='',next_page_xpath='',get_next_month=False,click_next_month=False,wait_after_loading=False)
            for link in self.events_list(event_links_xpath="//h2[contains(@class,'unical-calendar__event-title')]/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring='calendar.howard.edu/event'):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'event-title')]"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-body')]").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-left-col')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    #     item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//h1[contains(@class,'event-title')]/following-sibling::p").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//h1[contains(@class,'event-title')]/following-sibling::p").text
                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-right-col')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-right-col')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text

                    # item_data['startups_contact_info'] = ''
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
