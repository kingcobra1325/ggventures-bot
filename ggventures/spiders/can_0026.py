from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0026Spider(GGVenturesSpider):
    name = 'can_0026'
    start_urls = ["https://schulich.yorku.ca/about/contact-directory/"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "York University,Schulich School of Business"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Schulich_School_logo.png/220px-Schulich_School_logo.png"

    parse_code_link = "https://calendar.schulich.yorku.ca/"

    university_contact_info_xpath = "//p[text()='For general inquiries, please contact us at:']/.."
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//div[@class='lw_events_title']/a"):
            # for link in self.multi_event_pages(event_links_xpath="//a[starts-with(@class,'fc-event')]",next_page_xpath="//td[@class='fc-header-left']//span[@class='ui-icon ui-icon-circle-triangle-e']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://calendar.schulich.yorku.ca/event/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@id='lw_cal_events']/h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@id='lw_cal_event_rightcol']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[starts-with(@class,'lw_date_range')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='lw_cal_time_range']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//h5[@id='lw_cal_this_day']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='lw_start_time']/..").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h3[text()='Contact Info:']/following-sibling::p").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
