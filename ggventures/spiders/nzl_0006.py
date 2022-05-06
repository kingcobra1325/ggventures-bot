from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Nzl0006Spider(GGVenturesSpider):
    name = 'nzl_0006'
    start_urls = ["https://www.canterbury.ac.nz/business/contact-us/"]
    country = 'New Zealand'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Canterbury,College of Business and Economics"
    
    static_logo = "https://i.pinimg.com/736x/9c/e0/c0/9ce0c09e133225f9f034e801bdfdedfc.jpg"

    parse_code_link = "https://www.canterbury.ac.nz/events/list-events/"

    university_contact_info_xpath = "//h4[text()='Te Kura Umanga | UC Business School ']/.."
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            # for link in self.events_list(event_links_xpath="//li[contains(@style,'list-item')]//h3//a"):
            for link in self.multi_event_pages(event_links_xpath="//li[contains(@style,'list-item')]//h3//a",next_page_xpath="//ul[@class='simplePagerNav']",page_element="//a",current_page_class="rel",click_next_month=True,wait_after_loading=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.canterbury.ac.nz/events/active/uc-events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='events-single']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='nd-hide-900']/..").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[text()=' Date:']/..").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[text()=' Time:']/..").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[text()=' Date: ']/..").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[text()=' Time:']/..").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//li[@class='name']/..").text
                        # item_data['startups_link'] = self.getter.find_element(By.XPATH,"//label[@class='bt-label']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
