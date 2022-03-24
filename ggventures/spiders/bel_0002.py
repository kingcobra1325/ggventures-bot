from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Bel0002Spider(GGVenturesSpider):
    name = 'bel_0002'
    start_urls = ['https://www.antwerpmanagementschool.be/en/']
    country = "Belgium"
    eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "UAMS - Universiteit Antwerpen Management School"
    static_logo = "https://www.eicaa.eu/wp-content/uploads/2021/04/logo-ams.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.antwerpmanagementschool.be/en/events"

    university_contact_info_xpath = "//div[contains(@class,'o-flex')]//div[contains(@class,'u-bg-grey-lighter o-box')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//h4[contains(text(),'A PHP Error was encountered')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/parent::a",next_page_xpath="//a[contains(@title,'Go to next page')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//div[contains(@class,'event-filter')]//div[contains(@class,'teaser-outer')]/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=['agenda.kuleuven.be/en/content']):
            #
            #         logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #         item_data = self.item_data_empty.copy()
            #
            #         item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
            #         item_data['event_desc'] = self.getter.find_element(By.XPATH,"//article[contains(@class,'view-mode-full')]").text
            #
            #         item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").get_attribute('textContent')
            #         item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").get_attribute('textContent')
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
            #         #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'peoplePicker')]/parent::div").text
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
