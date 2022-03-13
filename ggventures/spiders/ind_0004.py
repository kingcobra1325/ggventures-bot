from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Ind0004Spider(GGVenturesSpider):
    name = 'ind_0004'
    start_urls = ['https://bkschool.org.in/']
    country = "India"
    # eventbrite_id = 30819498834
    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "B.K. School of Management"
    static_logo = "https://bkschool.org.in/wp-content/uploads/2019/11/bk-logo3.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://amrita.edu/events/"

    university_contact_info_xpath = "//h4[contains(text(),'Contact Us')]/following-sibling::div"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//span[contains(text(),'Invalid express')]")

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h4[contains(@class,'event-teaser')]/a",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'news-page')]//div[contains(@class,'news')]/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['amrita.edu/events']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h2[contains(@class,'banner-title')]"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'detail-box-desc')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-meta')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-meta')]").text

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
