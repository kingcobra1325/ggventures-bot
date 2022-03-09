from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0017Spider(GGVenturesSpider):
    name = 'can_0017'
    start_urls = ["https://haskayne.ucalgary.ca/contacts/directory"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Calgary,Haskayne School of Business"
    
    static_logo = "https://crunchbase-production-res.cloudinary.com/image/fetch/s--wuEAmLGW--/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Haskayne_School_of_Business.svg/375px-Haskayne_School_of_Business.svg.png"

    parse_code_link = "https://haskayne.ucalgary.ca/events"

    university_contact_info_xpath = "//main[@id='content']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//p[@class='title']/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://haskayne.ucalgary.ca/events"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='date']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='time']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='time']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='time']").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'contact_info_section')]").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
