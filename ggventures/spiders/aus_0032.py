from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Aus0032Spider(GGVenturesSpider):
    name = 'aus_0032'
    start_urls = ["https://www.uwa.edu.au/schools/Business#anchor-Contact-1EEA3E30-9415-4F5A-8B26-75272799527B"]
    country = 'Australia'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Western Australia,Business School"
    
    static_logo = "https://www.uwa.edu.au/Assets/Foundation/Assets/img/UWA-logo.svg"

    parse_code_link = "https://www.uwa.edu.au/study/events"

    university_contact_info_xpath = "//div[@class='info-snippet-module__info-snippets item-count-4']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            for link in self.events_list(event_links_xpath="//div[@class='results-list']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.uwa.edu.au/study/Events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='_title']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='event-details-module']/section/div[2]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//h4[text()='Date and time']/following-sibling::div").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//h4[text()='Date and time']/following-sibling::div").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text

                    # item_data['startups_contact_info'] = ''
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
