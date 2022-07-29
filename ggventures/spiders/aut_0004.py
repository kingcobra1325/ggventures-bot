from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Aut0004Spider(GGVenturesSpider):
    name = 'aut_0004'
    start_urls = ['https://www.wu.ac.at/studium/incoming-students/marketing-spring-program/universities-locations']
    country = "Austria"
    # eventbrite_id = 30819498834

    handle_httpstatus_list = [301,302,403,404]

    static_name = "Wirtschaftsuniversität Wien (WU),Vienna University of Economics & Business Administration"
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Logo_Wirtschaftsuniversit%C3%A4t_Wien.svg/800px-Logo_Wirtschaftsuniversit%C3%A4t_Wien.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.wu.ac.at/en/the-university/news-and-events/events"

    university_contact_info_xpath = ""
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'site-content')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'load-more')]",run_script=True)
            for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h2/a",next_page_xpath="//a[contains(@aria-label,'next month')]",get_next_month=True,click_next_month=True,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//div[contains(@class,'event-filter')]//div[contains(@class,'teaser-outer')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.wu.ac.at/en/the-university/news-and-events']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'md-text')]").text

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'md-eventteaser--detail')]").text
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'md-eventteaser--detail')]").text

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'peoplePicker')]/parent::div").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
