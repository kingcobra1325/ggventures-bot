from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0006Spider(GGVenturesSpider):
    name = 'can_0006'
    start_urls = ["https://www.mcgill.ca/desautels/about/contact"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "McGill University,Desautels Faculty of Management"
    
    static_logo = "https://mbatube.com/themes/mbatube/logos/1a5ab941da189d4794298d4412d6ec6d1584435255.jpg"

    parse_code_link = "https://www.mcgill.ca/desautels/events"

    university_contact_info_xpath = "//div[@id='content']//div[@class='field-items']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.ClickMore(click_xpath="//span[text()='Load More']")

            for link in self.events_list(event_links_xpath="//div[@class='preview']//a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.mcgill.ca/desautels/channels/event/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@id='page-title']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='channels-body-images']/following-sibling::div").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='custom-multi-date']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//hr/following-sibling::h5").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h4[text()='Contact']/following-sibling::p/a").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
