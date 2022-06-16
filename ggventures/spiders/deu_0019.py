from time import sleep

from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchAttributeException


class Deu0019Spider(GGVenturesSpider):
    name = 'deu_0019'
    start_urls = ["https://www.uni-bayreuth.de/en/contact"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False
    TRANSLATE = False

    static_name = "Universität Bayreuth"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Universit%C3%A4t_Bayreuth.svg/1280px-Universit%C3%A4t_Bayreuth.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uni-bayreuth.de/en/events-calender"

    university_contact_info_xpath = "//section"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.driver.get((self.driver.find_element(By.XPATH,"//a[@title='New window: ']").get_attribute('href')).replace('suche','en/search'))
            
            self.ClickMore(click_xpath="//div[starts-with(@class,'text-center')]/button")

            # for link in self.multi_event_pages(event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//article/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://region-bayreuth.de/en/event/"]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_desc'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[@itemprop='description']"))).get_attribute('textContent')

                    # item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'box-event-doc-header-date')]").text
                    # item_data['event_time'] = self.getter.find_element(By.XPATH,"//dl[contains(@class,'contact-list')]").text

                    try:
                        item_data['event_date'] = self.get_datetime_attributes("//table[@aria-label='date and time']//meta",datetime_attribute='content')
                        item_data['event_time'] = self.get_datetime_attributes("//table[@aria-label='date and time']//meta",datetime_attribute='content')
                    except (NoSuchElementException,NoSuchAttributeException) as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # logger.debug(f"XPATH not found {e}: Skipping.....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    try:
                        item_data['startups_contact_info'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[starts-with(@class,'organizer ')]"))).get_attribute('textContent')
                    except NoSuchElementException as e:
                        logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
