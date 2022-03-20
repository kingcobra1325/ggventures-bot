from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Esp0004Spider(GGVenturesSpider):
    name = 'esp_0004'
    start_urls = ['https://m.facebook.com/profile.php?id=184081228285686/']
    country = "Spain"
    # eventbrite_id = 30819498834

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "EAE - Escuela de Administración de Empresas"
    static_logo = "https://www.logolynx.com/images/logolynx/02/0235b4c5ed9d751b8bc7ea950d922ac0.jpeg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.eae.es/en/news/events"

    university_contact_info_xpath = "//div[contains(@class,'footer-card__content')]//a[contains(@class,'footer-contact')]//span"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'site-content')]",empty_text=True)

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[contains(@class,'overview-normal')]/a",next_page_xpath="//a[contains(@class,'loadMoreButton')]",get_next_month=False,click_next_month=True,wait_after_loading=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'list-events')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['eae.es/en/news/events']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1/span"))).get_attribute('textContent')
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'l-lp__content')]/section").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'time__content')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'time__content')]").text

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
