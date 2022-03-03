from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0014Spider(GGVenturesSpider):
    name = 'fra_0014'
    start_urls = ['https://www.rennes-sb.com/']
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "ESC Rennes School of Business"
    static_logo = "https://study-eu.s3.amazonaws.com/uploads/university/rennes-school-of-business-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.rennes-sb.com/agenda/"

    university_contact_info_xpath = "//div[contains(@class,'col contact-col')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//span[contains(text(),'Invalid express')]")

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[contains(@class,'dexp-grid-item')]//a",next_page_xpath="//span[contains(@class,'next-month')]/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//p[contains(@class,'unfr-hp-agenda__card__text')]/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['esc-clermont.fr/en']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'col content')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text.replace("\n"," ")
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'info')]").text
                    # try:
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'date-heure')]").text
                    # except NoSuchElementException as e:
                        # logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'date-heure')]").text

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
