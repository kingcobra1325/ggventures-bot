from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Pol0003Spider(GGVenturesSpider):
    name = 'pol_0003'
    start_urls = ['https://www.kozminski.edu.pl/en/contact']
    country = "Poland"
    # eventbrite_id = 30819498834

    # handle_httpstatus_list = [403,404]

    static_name = "LKAEM - Leon Kozminski Academy of Entrepreneurship and Management"
    static_logo = "https://studyqa.com/media/upload/univers/934/05/uni_profile_93405.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.kozminski.edu.pl/en/events"

    university_contact_info_xpath = "//section[contains(@class,'block-field-paragraphs')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(text(),'Wyświetlanie 0 - 0 z 0')]")

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[contains(@class,'overview-normal')]/a",next_page_xpath="//a[contains(@class,'loadMoreButton')]",get_next_month=False,click_next_month=True,wait_after_loading=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'button-wrapper')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['kozminski.edu.pl/en/events']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'body')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[contains(@class,'date')]").get_attribute('textContent')
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[contains(@class,'date')]").get_attribute('textContent')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//dt[contains(text(),'Contact')]/following-sibling::dd").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
