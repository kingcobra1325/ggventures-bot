from pydoc import cli
from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0036Spider(GGVenturesSpider):
    name = 'fra_0036'
    start_urls = ["https://www.sciencespo.fr/en/contact-map"]
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Sciences Po Paris"
    
    static_logo = "https://my.vioo.world/wp-content/uploads/2020/12/08234345/sciences_po.png"

    parse_code_link = "https://www.sciencespo.fr/evenements/"

    university_contact_info_xpath = "//div[starts-with(@class,'internal-page-module')]"
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            for link in self.events_list(event_links_xpath="//a[starts-with(@class,'push-event-module')]"):
            # for link in self.multi_event_pages(event_links_xpath="//div[@id='tab-future-events']//div[@class='col-12']/a",next_page_xpath="//li[@class='next']/a",click_next_month=True,run_script=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.sciencespo.fr/evenements/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='single-event-title']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='single-event-content-left']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='nd-hide-900']/..").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='inner-single-event-infos']//span[@class='label']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='inner-single-event-infos']//span[@class='value']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//p[@class='contact-item']/..").text
                    #     # item_data['startups_link'] = self.getter.find_element(By.XPATH,"//label[@class='bt-label']").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
