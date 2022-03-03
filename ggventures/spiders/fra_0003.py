from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0003Spider(GGVenturesSpider):
    name = 'fra_0003'
    start_urls = ['https://www.skema.edu/skema/access-and-contacts']
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'CERAM Sophia Antipolis'
    static_logo = 'https://www.skema.edu/_layouts/15/skema.internet.2016/site/branding/img/menu-logo.png?v=2.0'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://www.skema.edu/all-events'

    university_contact_info_xpath = "//div[contains(@class,'article-left')]"
    contact_info_text = True
    # contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'Sorry, no events for this category right now but check back later.')]")

            # for link in self.multi_event_pages(num_of_pages=5,event_links_xpath="//div[contains(@class,'about_right')]//li/a",next_page_xpath="//a[contains(text(),'Next')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'sk-allevents')]/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['skema.edu/skema-event']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='sk-title' and not(@id)]/h1"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'sk-description')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'sk-agenda-header')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'sk-agenda-header')]").text
                    # try:
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-detail__info--contact')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
