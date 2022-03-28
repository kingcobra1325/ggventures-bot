from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Deu0023Spider(GGVenturesSpider):
    name = 'deu_0023'
    start_urls = ["http://www.wvf.uni-freiburg.de/"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Universität Freiburg,Faculty of Economics and Behavioral Sciences"
    
    static_logo = "https://www.best-masters.com/assets/img/logo_ecole/838.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "http://www.wvf.uni-freiburg.de/weiterbildung-wissenschaftlicher-Nachwuchs"

    university_contact_info_xpath = "//div[@id='parent-fieldname-text']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.check_website_changed(upcoming_events_xpath="//p[text()='Meldung von Workshopwünschen sind jederzeit willkommen...']")

            # self.ClickMore(upcoming_events_xpath="//button[@class='filterable-list__load-more']")

            # for link in self.multi_event_pages(event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//div[starts-with(@class,'type-tribe_events')]/a"):

            #     self.getter.get(link)

            #     if self.unique_event_checker(url_substring=["https://www.wi.tum.de/event/"]):

            #         logger.info(f"Currently scraping --> {self.getter.current_url}")

            #         item_data = self.item_data_empty.copy()
                    
            #         item_data['event_link'] = link

            #         item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@Class='tribe-events-single-event-title']"))).text
            #         item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@id='tribe-events-header']/following-sibling::div").text

            #         # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'box-event-doc-header-date')]").text
            #         # item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'contact-list')]").text

            #         try:
            #             item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'tribe-events-single-section')]//dt[text()=' Date: ']/following-sibling::dd").text
            #             item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'tribe-events-single-section')]//dt[text()=' Time: ']/following-sibling::dd").text
            #         except NoSuchElementException as e:
            #             logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             # logger.debug(f"XPATH not found {e}: Skipping.....")
            #             item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #             item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

            #         try:
            #             item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//font[text()='Organizer']/ancestor::b/..").text
            #         except NoSuchElementException as e:
            #             logger.debug(f"XPATH not found {e}: Skipping.....")
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
