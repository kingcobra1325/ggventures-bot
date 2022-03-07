from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0009Spider(GGVenturesSpider):
    name = 'can_0009'
    start_urls = ["https://smith.queensu.ca/about/contact.php"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Queen's University,Queen's School of Business"
    
    static_logo = "https://smith.queensu.ca/_templates/images/content/grad_studies/mma/smith-logo-white.svg"

    parse_code_link = "https://smith.queensu.ca/recruiting/Events/index.php"

    university_contact_info_xpath = "//h2[text()='General Information']/.."
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//span[text()='Load More']")

            for link in self.driver.find_elements(By.XPATH,"//tbody/tr"):

                # self.getter.get(link)

                # if self.unique_event_checker(url_substring="https://www.mcgill.ca/desautels/channels/event/"):

                # logger.info(f"Currently scraping --> {self.getter.current_url}")

                item_data = self.item_data_empty.copy()

                item_data['event_name'] = WebDriverWait(link,20).until(EC.presence_of_element_located((By.XPATH,"./td[2]"))).get_attribute('textContent')
                # item_data['event_link'] = link
                try:
                    item_data['event_desc'] = link.find_element(By.XPATH,"./td[4]").text
                except NoSuchElementException as e:
                    logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['event_desc'] = link.find_element(By.XPATH,"").text

                try:
                    item_data['event_date'] = link.find_element(By.XPATH,"./td[1]").text
                    # item_data['event_time'] = link.find_element(By.XPATH,"./td[1]").text
                except NoSuchElementException as e:
                    logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                    # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h4[text()='Contact']/following-sibling::p/a").text
                # item_data['startups_link'] = ''
                # item_data['startups_name'] = ''

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
