from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Deu0015Spider(GGVenturesSpider):
    name = 'deu_0015'
    start_urls = ["https://www.en.som.lmu.de/ref_doks/kontakt/index.html"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "LMU München,Faculty of Business Administration"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/LMU_Muenchen_Logo.svg/1024px-LMU_Muenchen_Logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.lmu.de/en/newsroom/calendar-of-events/index.html"

    university_contact_info_xpath = "//div[starts-with(@class,'user-html')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            self.ClickMore(click_xpath="//button[@class='filterable-list__load-more']",run_script=True)

            # for link in self.multi_event_pages(event_links_xpath="//td/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=False,click_next_month=True,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//em[@class='filterable-list__list-item-meta']/../a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://www.lmu.de/en/newsroom/calendar-of-events/event/"]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='stage__event-box-headline']"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='rte__container']").text

                    # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'box-event-doc-header-date')]").text
                    # item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'contact-list')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[@class='stage__event-box-content-column-paragraph']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='stage__event-box-content']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # logger.debug(f"XPATH not found {e}: Skipping.....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//strong[text()='Contact']/../following-sibling::p").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
