from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0010Spider(GGVenturesSpider):
    name = 'can_0010'
    start_urls = ["https://www.smu.ca/academics/sobey/sobey-about-contact-us.html"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Saint Mary's University,Sobey School of Business"
    
    static_logo = "https://smuca-179a2.kxcdn.com/images/brandassets/logo/SMU_Sobey_4C_200x71.png"

    parse_code_link = "https://www.smu.ca/studentlife/index.html"

    university_contact_info_xpath = "//div[@class='cnt_block']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.ClickMore(click_xpath="//a[@translate='loadMoreEvents']")

            for link in self.events_list(event_links_xpath="//div[contains(@class,'agendaItem__image')]//a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://tockify.com/smuhalifax/detail/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'header')]"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='eventDetail__what']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'when')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'when')]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h4[text()='Contact']/following-sibling::p/a").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
