from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0016Spider(GGVenturesSpider):
    name = 'can_0016'
    start_urls = ["https://www.sauder.ubc.ca/contact-ubc-sauder"]
    country = 'Canada'
    eventbrite_id = 17946977554

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of British Columbia,Sauder School of Business"
    
    static_logo = "https://professional.sauder.ubc.ca/dap/images/myubcdap/logo_main.png"

    parse_code_link = "https://mybcom.sauder.ubc.ca/events"

    university_contact_info_xpath = "//div[@id='content']/following-sibling::div"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//h3/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://mybcom.sauder.ubc.ca/events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//article").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-single']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-single']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text

                    # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h4[text()='Contact']/following-sibling::p/a").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
