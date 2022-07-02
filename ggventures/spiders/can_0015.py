from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0015Spider(GGVenturesSpider):
    name = 'can_0015'
    start_urls = ["https://www.ualberta.ca/business/contact/index.html"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Alberta,School of Business"
    
    static_logo = "https://www.ualberta.ca/_assets/images/ua-logo-reversed-white.svg"

    parse_code_link = r"https://www.ualberta.ca/events/index.html#sort=relevancy&f:FacultyFacet=[Alberta%20School%20of%20Business]"

    university_contact_info_xpath = "//div[@class='row  ']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//span[text()='Load More']")

            for link in self.events_list(event_links_xpath="//div[@class='col-12']//a"):
            # for link in self.multi_event_pages(event_links_xpath="//a[@class='no-underline']",next_page_xpath="//div[starts-with(@class,'text-center')]//a/i/.."):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.ualberta.ca/events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='page-title']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//dl").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//i[@class='icon-calendar']/..").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//i[@class='icon-calendar']/..").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h4[text()='Contact']/following-sibling::p/a").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
