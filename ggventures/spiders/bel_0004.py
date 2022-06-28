from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Bel0004Spider(GGVenturesSpider):
    name = 'bel_0004'
    start_urls = ['https://sbsem.ulb.be/the-school/the-administrative-team']
    country = "Belgium"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Université Libre de Bruxelles,Solvay Business School"
    static_logo = "https://www.solvay.edu/wp-content/themes/solvay/img/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.solvay.edu/en/events/"

    university_contact_info_xpath = "//div[contains(@id,'description')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//h4[contains(text(),'A PHP Error was encountered')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[contains(@id,'uclcalendar_list_ajax')]//div[contains(@class,'list-image')]/a",next_page_xpath="//a[text()='next']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//section[contains(@class,'events-wrapper')]//h2/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['exed.solvay.edu']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()
                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text


                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//p[contains(@class,'fz-large')]/parent::div"],method='attr',error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event-infos')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event-infos')]"],method='attr',error_when_none=False)
                    
                    try:
                        # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'row agenda-infos')]//label[text()='Contact']/following-sibling::div").text
                        item_data['startups_contact_info'] = '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//strong[contains(text(),'estions')]/parent::span/parent::p/following-sibling::p")])
                    except NoSuchElementException as e:
                        logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'row agenda-infos')]//label[text()='Contact']/following-sibling::div"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
