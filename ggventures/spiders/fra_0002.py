from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Fra0002Spider(GGVenturesSpider):
    name = 'fra_0002'
    start_urls = ['https://student.kedge.edu/contact']
    country = 'France'
    # eventbrite_id = 1412983127
    TRANSLATE=True

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'Bordeaux Ecole de Management'
    static_logo = 'https://upload.wikimedia.org/wikipedia/commons/1/11/Logo_BEM_HD.jpg'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://panka.audencia.com/evenements?solr%5Bfilter%5D%5Blang%5D%5B0%5D=language_stringS%3Aen'

    university_contact_info_xpath = "//div[contains(@class,'article_tabs_content')]"
    contact_info_text = True
    # contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'Sorry, no events for this category right now but check back later.')]")

            # for link in self.multi_event_pages(num_of_pages=5,event_links_xpath="//div[contains(@class,'about_right')]//li/a",next_page_xpath="//a[contains(text(),'Next')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'solr-doc')]/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['www.audencia.com','international.audencia.com']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'col-video')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//ul[contains(@class,'event-infos')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//ul[contains(@class,'event-infos')]").text
                    # try:
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text

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
