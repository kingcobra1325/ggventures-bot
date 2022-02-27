from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Aus0031Spider(GGVenturesSpider):
    name = 'aus_0031'
    start_urls = ["https://www.usc.edu.au/about/structure/schools/school-of-business-and-creative-industries"]
    country = 'Australia'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'University of the Sunshine Coast (USC),Faculty of Business'
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/Logo_of_the_University_of_the_Sunshine_Coast.svg/440px-Logo_of_the_University_of_the_Sunshine_Coast.svg.png"

    parse_code_link = "https://www.usc.edu.au/community/events"

    university_contact_info_xpath = "//h4[text()='Enquiries']/.."
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            for link in self.events_list(event_links_xpath="//a[text()='MORE']"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.usc.edu.au/community/events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='text-center']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//article[@class='grid-area']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='event-summary-block'][2]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='event-summary-block']").text
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
