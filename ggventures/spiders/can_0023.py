from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0023Spider(GGVenturesSpider):
    name = 'can_0023'
    start_urls = ["https://www.uvic.ca/gustavson/about/about/contact/index.php"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Victoria,Faculty of Business"
    
    static_logo = "https://ft-bschool-rankings.s3.eu-west-2.amazonaws.com/production/images/8c4516e5-75dc-4f51-a957-8dfe56e8bc05-3262c7b2461fccf5ac6832b609251ca1"

    parse_code_link = "https://events.uvic.ca/gustavson/"

    university_contact_info_xpath = "//tbody"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//div[@class='event-highlight']//a"):
            # for link in self.multi_event_pages(event_links_xpath="//a[starts-with(@class,'fc-event')]",next_page_xpath="//td[@class='fc-header-left']//span[@class='ui-icon ui-icon-circle-triangle-e']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://events.uvic.ca/gustavson/event/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='event-body--summary']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='event-body--description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='event-datetime']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='event-datetime']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text


                    # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//p[@class='mb-0']").text
                        
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
