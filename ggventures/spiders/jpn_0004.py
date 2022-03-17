from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Jpn0004Spider(GGVenturesSpider):
    name = 'jpn_0004'
    start_urls = ['https://www.econ.hokudai.ac.jp/en/']
    country = "Japan"
    # eventbrite_id = 30819498834
    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Hokkaido University,Graduate School of Economics and Business Administration"
    static_logo = "https://www.global.hokudai.ac.jp/wp-content/themes/hokudaien/img/common/logo_large.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.doshisha.ac.jp/en/event/?mode=new"

    university_contact_info_xpath = "//section"
    # contact_info_text = True
    # contact_info_textContent = True
    contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'cmsmasters_column one_third')]",empty_text=True)

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h4[contains(@class,'event-teaser')]/a",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'cmn-newsSet')]//a[contains(@class,'link')]"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['www.doshisha.ac.jp/en/event']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h3"))).get_attribute('textContent')
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'pageContents')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'opening')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'opening')]").text

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//dt[contains(text(),'Contact')]/following-sibling::dd").text
                    except NoSuchElementException as e:
                        logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
