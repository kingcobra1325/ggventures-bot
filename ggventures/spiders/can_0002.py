from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0002Spider(GGVenturesSpider):
    name = 'can_0002'
    start_urls = ["https://sprott.carleton.ca/contact-us/"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Carleton University,Sprott School of Business"
    
    static_logo = "https://pbs.twimg.com/media/FMNgMxZWUAMuWGU?format=jpg&name=4096x4096"

    parse_code_link = "https://sprott.carleton.ca/events/"

    university_contact_info_xpath = "//main[@id='content']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//span[text()='Load More']",final_counter=3)

            for link in self.events_list(event_links_xpath="//li[@itemprop='item']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://sprott.carleton.ca/event/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//section/h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@id='content']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//dt[text()='Start']/following-sibling::dd").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//dt[text()='Time']/following-sibling::dd").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//dt[text()='Contact']/following-sibling::dd").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
