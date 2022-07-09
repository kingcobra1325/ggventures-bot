from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0034Spider(GGVenturesSpider):
    name = 'fra_0034'
    start_urls = ["https://www.iscparis.com/en/"]
    country = 'France'
    
    handle_httpstatus_list = [301,302,403,404]

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "ISC Paris"
    
    static_logo = "https://www.iscparis.com/wp-content/themes/limpide/assets/img/svg/logo-isc-red.svg"

    parse_code_link = "https://www.iscparis.com/en/evenement/"

    university_contact_info_xpath = "//div[@class='footer-block footer-block__contact footer-accordeon']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            # for link in self.events_list(event_links_xpath="//div[@class='extrait']/a"):
            for link in self.multi_event_pages(event_links_xpath="//div[@class='content-right']/h3/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.iscparis.com/en/evenement"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='post-title']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='is-container-small']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='nd-hide-900']/..").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='is-container-small']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='is-container-small']").text
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
