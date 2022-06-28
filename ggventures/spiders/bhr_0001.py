from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Bhr0001Spider(GGVenturesSpider):
    name = 'bhr_0001'
    start_urls = ['https://www.ucb.edu.bh/about/contact-us']
    country = "Bahrain"
    # eventbrite_id = 30819498834

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University College of Bahrain (UCB),School of Business"
    static_logo = "https://resources.finalsite.net/images/f_auto,q_auto,t_image_size_2/v1610653981/ucbedubh/he2vydau4rmt4mhad1ku/HomeLogoFinal.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ucb.edu.bh/ucb/all-posts"

    university_contact_info_xpath = "//div[@class='fsElement fsFormsElement']/following-sibling::div"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'site-content')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h2/a",next_page_xpath="//a[contains(@aria-label,'next month')]",get_next_month=True,click_next_month=True,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//article",return_elements=True):
                # self.getter.get(link)
                # if self.unique_event_checker(url_substring=['www.wu.ac.at/en/the-university/news-and-events']):

                    # logger.info(f"Currently scraping --> {self.getter.current_url}")

                item_data = self.item_data_empty.copy()

                item_data['event_name'] = link.find_element(By.XPATH,"./div[@class='fsTitle']").get_attribute('textContent')
                item_data['event_desc'] = link.get_attribute('textContent')

                item_data['event_date'] = link.get_attribute('textContent')
                item_data['event_time'] = link.get_attribute('textContent')

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
                # item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
