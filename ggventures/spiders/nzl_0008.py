from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from time import sleep

class Nzl0008Spider(GGVenturesSpider):
    name = 'nzl_0008'
    start_urls = ["https://www.wgtn.ac.nz/about"]
    country = 'New Zealand'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Victoria University of Wellington"
    
    static_logo = "https://www.wgtn.ac.nz/__data/assets/git_bridge/0005/1778018/dist/images/new/v2/logo-white-full.svg?v=2"

    parse_code_link = "https://www.wgtn.ac.nz/events"

    university_contact_info_xpath = "//ul[@class='contacts']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            # for link in self.events_list(event_links_xpath="//h3/a"):
            sleep(5)
            for link in self.multi_event_pages(event_links_xpath="//h3//a",next_page_xpath="//i[@class='icons8-forward']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://www.wgtn.ac.nz/events","https://www.wgtn.ac.nz/chinaresearchcentre","https://www.wgtn.ac.nz/wfadi/",
                                                            "https://www.wgtn.ac.nz/som",]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//main//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'desc')]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='nd-hide-900']/..").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='time']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='time']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//h5[@id='lw_cal_this_day']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='lw_start_time']/..").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//label[text()='Contact']/..").text
                        item_data['startups_link'] = self.getter.find_element(By.XPATH,"//label[@class='bt-label']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
