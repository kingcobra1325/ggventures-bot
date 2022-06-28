from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Deu0020Spider(GGVenturesSpider):
    name = 'deu_0020'
    start_urls = ["https://www.uni-due.de/ub/en/ewiwi.shtml"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Universität Duisburg-Essen,Faculty of Economics"
    
    static_logo = "https://www.myscience.de/var/mysciencede/image/logo/uni-due.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uni-due.de/gcplus/en/events.php"

    university_contact_info_xpath = "//span[text()='Contact']/../.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.ClickMore(upcoming_events_xpath="//button[@class='filterable-list__load-more']")

            # for link in self.multi_event_pages(event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in range(1,len(self.driver.find_elements(By.XPATH,"//div[starts-with(@class,'h2')]"))+1):

                # self.getter.get(link)

                # if self.unique_event_checker(url_substring=["https://www.wi.tum.de/event/"]):

                logger.info(f"Currently scraping --> {response.url}")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = response.url

                item_data['event_name'] = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,f"//div[starts-with(@class,'h2')][{link}]/following-sibling::h2"))).text
                item_data['event_desc'] = self.driver.find_element(By.XPATH,f"//div[starts-with(@id,'beschreibung')][{link}]").get_attribute('textContent')

                # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'box-event-doc-header-date')]").text
                # item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'contact-list')]").text

                try:
                    item_data['event_date'] = self.driver.find_element(By.XPATH,f"//div[starts-with(@class,'h2')][{link}]/following-sibling::p").text
                    item_data['event_time'] = self.driver.find_element(By.XPATH,f"//div[starts-with(@class,'h2')][{link}]/following-sibling::p").text
                except NoSuchElementException as e:
                    logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # logger.debug(f"XPATH not found {e}: Skipping.....")
                    item_data['event_date'] = self.driver.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    item_data['event_time'] = self.driver.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                try:
                    item_data['startups_contact_info'] = self.driver.find_element(By.XPATH,f"//div[starts-with(@class,'h2')][{link}]/following-sibling::div//ul").get_attribute('textContent')
                except NoSuchElementException as e:
                    logger.debug(f"XPATH not found {e}: Skipping.....")
                # item_data['startups_link'] = ''
                # item_data['startups_name'] = ''

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
