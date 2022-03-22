from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Deu0012Spider(GGVenturesSpider):
    name = 'deu_0012'
    start_urls = ["https://www.hhl.de/"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "HHL Leipzig,Leipzig Graduate School of Management"
    
    static_logo = "https://www.hhl.de/app/uploads/2021/11/HHL_L_Gray_CMYK.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.hhl.de/experience/life-at-hhl/campus-events/"

    university_contact_info_xpath = "//div[@class='navigationFooter-phone']/.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//span[contains(text(),'Invalid express')]")

            # for link in self.multi_event_pages(event_links_xpath="//td/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=False,click_next_month=True,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//h3[@class='eventTeaser-title']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://www.hhl.de/event/"]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='heroEvent-title']"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//main[starts-with(@class,'mainContent')]").get_attribute('textContent')

                    # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'box-event-doc-header-date')]").text
                    # item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'contact-list')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[text()='When:']/.. | //strong[text()='When?']/../following-sibling::p | //p[@class='eventTeaser-date']").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[text()='When:']/.. | //strong[text()='When?']/../following-sibling::p").get_attribute('textContent')
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # logger.debug(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//strong[text()='Contact']/../following-sibling::p").text
                    except NoSuchElementException as e:
                        logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
