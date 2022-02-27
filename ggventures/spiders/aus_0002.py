from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Aus0002Spider(GGVenturesSpider):

    name = 'aus_0002'
    country = 'Australia'
    start_urls = ["https://bond.edu.au/intl/about-bond/academia/bond-business-school"]
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'Bond University,School of Business'
    static_logo = 'https://static.bond.edu.au/sites/all/themes/bond_base/logo.svg'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://bond.edu.au/intl/events'

    university_contact_info_xpath = "//h2[text()='Contact us']/.."
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'Sorry, no events for this category right now but check back later.')]")

            # # for link in self.multi_event_pages(self,num_of_pages=6,event_links_xpath='',next_page_xpath='',get_next_month=False,click_next_month=False,wait_after_loading=False)
            # for link in self.events_list(event_links_xpath="//h4[@class='timeline-title']/a"):
            #
            #     self.getter.get(link)
            #
            #     if self.unique_event_checker(url_substring='calendar.howard.edu/event'):
            #
            #         logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #         item_data = self.item_data_empty.copy()
            #
            #         item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
            #         item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='container']/article").text
            #         # try:
            #         #     item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-left-col')]").text
            #         # except NoSuchElementException as e:
            #         #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #         #     item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text
            #
            #         item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='day_month_year']").text
            #         item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[@class='time']").text
            #         # try:
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-right-col')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'event-right-col')]").text
            #         # except NoSuchElementException as e:
            #         #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//time[contains(@data-automation,'event-details-time')]").text
            #
            #         item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h3[text()='Contact']/..").text
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''
            #         item_data['event_link'] = link
            #
            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
