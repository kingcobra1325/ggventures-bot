from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0022Spider(GGVenturesSpider):
    name = 'fra_0022'
    start_urls = ["https://eslsca.edu.eg/"]
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "ESLSCA"
    
    static_logo = "https://eslsca.edu.eg/wp-content/uploads/2020/06/Eslsca-Logo.png"

    parse_code_link = "https://www.esdes.fr/en/welcome/about-esdes/newsroom/all-the-events/"

    university_contact_info_xpath = "//a[contains(text(),'admission')]"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//button[text()='View more events']")

            for link in self.events_list(event_links_xpath="//div[@class='content-event-image-wrapper']/.."):
            # for link in self.multi_event_pages(event_links_xpath="//h3//a",next_page_xpath="//i[@class='icons8-forward']",click_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.esdes.fr/en/welcome/about-esdes/newsroom/all-the-events"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='text-banner']"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[starts-with(@class,'page-content')]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='nd-hide-900']/..").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@data-column-clickable]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@data-column-clickable]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//h5[@id='lw_cal_this_day']").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='lw_start_time']/..").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//p[@class='contact-item']/..").text
                        # item_data['startups_link'] = self.getter.find_element(By.XPATH,"//label[@class='bt-label']").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                    item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
