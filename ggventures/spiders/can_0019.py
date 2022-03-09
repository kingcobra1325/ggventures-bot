from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0019Spider(GGVenturesSpider):
    name = 'can_0019'
    start_urls = ["https://www.unb.ca/contact/"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of New Brunswick - Saint John"
    
    static_logo = "https://www.unb.ca/webcomps/_css/unb_logo_white.png"

    parse_code_link = "https://www.unb.ca/event-calendar/"

    university_contact_info_xpath = "//h3[text()='UNB Saint John']/.."
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            # for link in self.events_list(event_links_xpath="//a[starts-with(@class,'fc-event')]"):
            for link in self.multi_event_pages(event_links_xpath="//a[starts-with(@class,'fc-event')]",next_page_xpath="//td[@class='fc-header-left']//span[@class='ui-icon ui-icon-circle-triangle-e']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.unb.ca/event-calendar/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='event-details']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[text()='Event Date(s):']/following-sibling::div").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[text()='Time(s):']/following-sibling::div").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[@class='event-contact']").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
