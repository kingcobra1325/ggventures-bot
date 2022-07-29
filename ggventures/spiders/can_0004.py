from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0004Spider(GGVenturesSpider):
    name = 'can_0004'
    start_urls = ["https://www.dal.ca/contact_us.html"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Dalhousie University"
    
    static_logo = "https://cdn.dal.ca/etc/designs/dalhousie/clientlibs/global/default/images/logos/dalhousie-logo-black.svg.lt_03b76acfc2f5fdf8c1ce5ef80071ef35.res/dalhousie-logo-black.svg"

    parse_code_link = "https://events.dal.ca/"

    university_contact_info_xpath = "//div[@class='maincontent']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//span[text()='Load More']",final_counter=3)

            for link in self.events_list(event_links_xpath="//div[@class='lw_events_title']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://events.dal.ca/event/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@id='lw_cal_events']/h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='span8']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//h5[@id='lw_cal_this_day']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='lw_start_time']/..").text
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
