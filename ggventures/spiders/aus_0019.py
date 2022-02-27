from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Aus0019Spider(GGVenturesSpider):
    name = 'aus_0019'
    start_urls = ['https://cbe.anu.edu.au/welcome-cbe/']
    country = 'Australia'
    eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    # static_name = ''
    static_logo = 'https://cbe.anu.edu.au/sites/default/files/2x_anu_logo_small_over.png'

    parse_code_link = 'https://cbe.anu.edu.au/events'

    university_contact_info_xpath = "//section[contains(@id,'contactdetails')]"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            for link in self.events_list(event_links_xpath="//div[contains(@class,'news-right')]/h3/a"):

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

                    # item_data['startups_contact_info'] = ''
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
