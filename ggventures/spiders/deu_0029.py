from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Deu0029Spider(GGVenturesSpider):
    name = 'deu_0029'
    start_urls = ["https://www.uni-osnabrueck.de/en/service-sites/contact/"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Universität Osnabrück"
    
    static_logo = "https://cdn.signavio.com/uploads/2013/03/Logo-Universitaet-Osnabrueck.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uni-osnabrueck.de/en/events/key-events-at-osnabrueck-university/"

    university_contact_info_xpath = "//div[@class='eb2']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.ClickMore(upcoming_events_xpath="//button[@class='filterable-list__load-more']")

            # for link in self.multi_event_pages(event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'col_4')]//a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://www.uni-osnabrueck.de/en/events/"]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='eb2']/h2"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='eb2']").text

                    # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'box-event-doc-header-date')]").text
                    # item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'contact-list')]").text

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'tribe-events-single-section')]//dt[text()=' Date: ']/following-sibling::dd").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'tribe-events-single-section')]//dt[text()=' Time: ']/following-sibling::dd").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'contact')] | //strong[contains(text(),'Contact')]/..").text
                    except NoSuchElementException as e:
                        logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
