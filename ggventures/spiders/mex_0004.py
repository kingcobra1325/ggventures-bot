from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Mex0004Spider(GGVenturesSpider):
    name = 'mex_0004'
    start_urls = ['https://egade.tec.mx/en/form/contact']
    country = "Mexico"
    # eventbrite_id = 30819498834

    # handle_httpstatus_list = [403,404]

    static_name = "ITESM - Campus Monterrey,EGADE"
    static_logo = "https://pbs.twimg.com/profile_images/916329370360279040/NsfJ-3ut_400x400.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ipadebusinessschool.com/category/events/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'ullcalendar-container')]//a[not(text()='next') and not(text()='previous')]",checking_if_none=True)

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[contains(@class,'overview-normal')]/a",next_page_xpath="//a[contains(@class,'loadMoreButton')]",get_next_month=False,click_next_month=True,wait_after_loading=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'c-events-blog')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['egade.tec.mx/es/node','egade.tec.mx/en/node']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'name__title')]"))).get_attribute('textContent')
                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-event-information-name__text')]").get_attribute('textContent')

                    item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-event-information-date')]").get_attribute('textContent')
                    item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-event-information-date')]").get_attribute('textContent')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//dt[contains(text(),'Contact')]/following-sibling::dd").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
