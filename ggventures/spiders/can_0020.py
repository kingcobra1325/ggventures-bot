from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0020Spider(GGVenturesSpider):
    name = 'can_0020'
    start_urls = ["https://telfer.uottawa.ca/en/contact/"]
    country = 'Canada'
    eventbrite_id = 1483760122

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Ottawa,Telfer School of Management"
    
    static_logo = "https://www.thembatour.com/profile/College/392/Telfer_logo_cropped.png"

    parse_code_link = "https://telfer.uottawa.ca/en/events/"

    university_contact_info_xpath = "//div[@itemprop='articleBody']//div[@class='container']//div[@class='row']"
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//a[@class='u-url']"):
            # for link in self.multi_event_pages(event_links_xpath="//a[starts-with(@class,'fc-event')]",next_page_xpath="//td[@class='fc-header-left']//span[@class='ui-icon ui-icon-circle-triangle-e']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://telfer.uottawa.ca/en/events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'event-description')]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[@class='mb-2']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//p[@class='mb-2']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//p[@class='mb-0']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
