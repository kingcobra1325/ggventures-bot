from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Cze0004Spider(GGVenturesSpider):
    name = 'cze_0004'
    start_urls = ['https://pibs.cz/showdoc.do?docid=84/']
    country = "Czech Republic"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Prague International Business School (PIBS)"
    static_logo = "https://www.eduopinions.com/wp-content/uploads/2020/05/Prague-International-Business-School-logo.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.fbm.vutbr.cz/en/faculty/event-calendar"

    university_contact_info_xpath = "//div[contains(@class,'b-contact--primary')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[contains(@id,'uclcalendar_list_ajax')]//div[contains(@class,'list-image')]/a",next_page_xpath="//a[text()='next']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//a[contains(@class,'scroll-item')]"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=['zsem.hr/en/events']):
            #
            #         logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #         item_data = self.item_data_empty.copy()
            #
            #         item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
            #         item_data['event_desc'] = self.getter.find_element(By.XPATH,"//section[contains(@class,'section-text')]").get_attribute('textContent')
            #
            #         item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[contains(@class,'title-label')]").get_attribute('textContent')
            #         item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[contains(@class,'title-label')]").get_attribute('textContent')
            #
            #         # try:
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
            #         # except NoSuchElementException as e:
            #         #     logger.debug(f"XPATH not found {e}: Skipping.....")
            #         #     # logger.debug(f"XPATH not found {e}: Skipping.....")
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #
            #         # try:
            #         #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-contact-card')]").text
            #         # except NoSuchElementException as e:
            #         #     logger.debug(f"XPATH not found {e}: Skipping.....")
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''
            #         item_data['event_link'] = link
            #
            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
