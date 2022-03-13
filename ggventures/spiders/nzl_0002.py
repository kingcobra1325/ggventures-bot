from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Nzl0002Spider(GGVenturesSpider):
    name = 'nzl_0002'
    start_urls = ["https://www.aut.ac.nz/about/faculties-and-schools/faculty-of-business,-economics-and-law/contact-the-faculty-business,-economics-and-law"]
    country = 'New Zealand'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Lincoln University,Commerce Division"
    
    static_logo = "https://www.lincoln.ac.nz/_resources/themes/app/dist/images/logo-Lincoln.svg?m=1643663488"

    parse_code_link = "https://www.lincoln.ac.nz/news-and-events/?sortBy=date_published&term3=4"

    university_contact_info_xpath = "//div[@id='mainContent']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//ul[@data-cy='results-list']//a"):
            # for link in self.multi_event_pages(event_links_xpath="//a[starts-with(@class,'fc-event')]",next_page_xpath="//td[@class='fc-header-left']//span[@class='ui-icon ui-icon-circle-triangle-e']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.lincoln.ac.nz/news-and-events/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='element-content']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//p/span[starts-with(@class,'inline')]").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//th[text()='Date:']/following-sibling::td").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//h5[@id='lw_cal_this_day']").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='lw_start_time']/..").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h3[text()='Contact Info:']/following-sibling::p").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
