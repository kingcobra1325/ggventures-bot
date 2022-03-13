from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Ind0002Spider(GGVenturesSpider):
    name = 'ind_0002'
    start_urls = ['https://www.amity.edu/abs/']
    country = "India"
    # eventbrite_id = 30819498834
    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Amity Business School"
    static_logo = "https://www.dialeducation.com/assets/images/college/logo_1566036989.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.alliance.edu.in/events"

    university_contact_info_xpath = "//div[contains(@class,'contact_full-width')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//span[contains(text(),'Invalid express')]")

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h4[contains(@class,'event-teaser')]/a",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'events')]//a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['www.alliance.edu.in/events']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'event-heading')]"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-main')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//h1[contains(@class,'event-heading')]/parent::div").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//h1[contains(@class,'event-heading')]/parent::div").text

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'contact-info')]/dl").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
