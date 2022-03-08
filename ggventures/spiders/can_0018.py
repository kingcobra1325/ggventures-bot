from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0018Spider(GGVenturesSpider):
    name = 'can_0018'
    start_urls = ["https://umanitoba.ca/asper/"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Manitoba,Asper School of Business"
    
    static_logo = "https://give.umanitoba.ca/image/logos/12_AsperLogo_horz.png"

    parse_code_link = "https://eventscalendar.umanitoba.ca/"

    university_contact_info_xpath = "//div[@class='contact__details']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//li[starts-with(@class,'pager-next')]")

            for link in self.events_list(event_links_xpath="//a[@itemprop='url']"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://eventscalendar.umanitoba.ca/site/asper/event/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h2[@itemprop='name']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@itemprop='description']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='lw_calendar_event_description']").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//section[@class='event-detail-date']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//section[@class='event-detail-date']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='date-display-range']").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//section[@class='event-detail-contact-person']").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
