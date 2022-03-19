from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0030Spider(GGVenturesSpider):
    name = 'fra_0030'
    start_urls = ["https://www.insead.edu/get-in-touch"]
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "INSEAD"
    
    static_logo = "https://www.insead.edu/sites/all/themes/insead_theme/img/logo_roundel.png"

    parse_code_link = "https://www.insead.edu/events"

    university_contact_info_xpath = "//div[@class='container-fluid']"
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'widgetbox')]/a"):
            # for link in self.multi_event_pages(event_links_xpath="//h3//a",next_page_xpath="//i[@class='icons8-forward']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://www.insead.edu/centres/","https://www.insead.edu/events/"]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='heading3']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@role='tabpanel']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='panel-separator']/following-sibling::div").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'sepline')]/following-sibling::h3 | //h3[@class='mbot0']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'sepline')]/following-sibling::h3").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]").text

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
