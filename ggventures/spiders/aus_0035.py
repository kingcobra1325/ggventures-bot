from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Aus0035Spider(GGVenturesSpider):
    name = 'aus_0035'
    start_urls = ["https://www.uow.edu.au/business-law/contact-us/"]
    country = 'Australia'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Victoria University,Victoria Graduate School of Business"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/2/25/Victoria_University_Melb_Aus_Logo_Master_K_reduced.jpg"

    parse_code_link = "https://www.vu.edu.au/about-vu/news-events/events"

    university_contact_info_xpath = "//section[starts-with(@class,'page-content')]"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            for link in self.events_list(event_links_xpath="//span[@class='field-content']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.vu.edu.au/about-vu/news-events/events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='page-header']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='event-body-text']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[text()='When:']/../..").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[text()='When:']/../..").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    #item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h3[text()='Contact us']/..").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
