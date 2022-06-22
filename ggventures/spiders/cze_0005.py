from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Cze0005Spider(GGVenturesSpider):
    name = 'cze_0005'
    start_urls = ['https://www.vse.cz/english/']
    country = "Czech Republic"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University Of Economics Prague"
    static_logo = "https://www.vse.cz/english/wp-content/themes/vse-redesigned/dist/img/logo/logo-full-en-white.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://kalendar.vse.cz/english/"

    university_contact_info_xpath = "//footer[contains(@class,'footer-address')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2/a",next_page_xpath="//div[contains(@class,'nav-calendar-next')]/a",get_next_month=True,click_next_month=False,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//a[contains(@class,'scroll-item')]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['kalendar.vse.cz/english/event']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
                    # item_data['event_desc'] = self.getter.find_element(By.XPATH,"//table[contains(@class,'event-detail-basic-info')]/following-sibling::div").text
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//table[contains(@class,'event-detail-basic-info')]/following-sibling::div").text
                    except NoSuchElementException as e:
                        logger.debug(f"XPATH not found {e}: Skipping.....")

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//table[contains(@class,'event-detail-basic-info')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//table[contains(@class,'event-detail-basic-info')]").text

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-contact-card')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
