from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0003Spider(GGVenturesSpider):
    name = 'can_0003'
    start_urls = ["https://www.concordia.ca/jmsb/programs/graduate/contact-us.html"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Concordia University,John Molson School of Business"
    
    static_logo = "https://icmrindia.org/just-in-case/Newsletter/image/logo6.jpg"

    parse_code_link = "https://www.concordia.ca/jmsb/events.html"

    university_contact_info_xpath = "//div[@class='rte']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//span[text()='Load More']",final_counter=3)

            for link in self.events_list(event_links_xpath="//div[@class='rte']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.concordia.ca/cuevents/jmsb/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='event-title']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='span8']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='info-text']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='info-text']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h6[text()='CONTACT']/following-sibling::p").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)