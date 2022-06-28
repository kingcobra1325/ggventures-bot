from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Fra0004Spider(GGVenturesSpider):
    name = 'fra_0004'
    start_urls = ['https://www.edcparis.edu/en/contact']
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "EDC - Ecole des Dirigeants & Créateurs d'entreprise"
    static_logo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/EDC_PARIS_BUSINESS_SCHOOL_LOGO_MONOCHROME_BLEU.png/440px-EDC_PARIS_BUSINESS_SCHOOL_LOGO_MONOCHROME_BLEU.png'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://www.edcparis.edu/en/events'

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            self.check_website_changed(upcoming_events_xpath="//h2[@class='not-found-title']")

            # for link in self.multi_event_pages(num_of_pages=5,event_links_xpath="//div[contains(@class,'about_right')]//li/a",next_page_xpath="//a[contains(text(),'Next')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//h2[@class='entry-title']//a"):
            
            #     self.getter.get(link)
            
            #     if self.unique_event_checker(url_substring=['edcparis.edu/en/events']):
            
            #         logger.info(f"Currently scraping --> {self.getter.current_url}")
            
            #         item_data = self.item_data_empty.copy()
            
            #         # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

            #         item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='et_pb_title_container']/parent::div/parent::div"],method='attr')
            #         item_data['event_desc'] = self.scrape_xpath(xpath_list=["//h2/parent::div"],method='attr')
            #         item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='et_pb_title_container']/parent::div/parent::div/parent::div"],method='attr')
            #         item_data['event_time'] = self.scrape_xpath(xpath_list=["//h2/parent::div"],method='attr')
            #         # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
            #         # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

            #         # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[contains(text(),'CONTACT')]/following-sibling::p"],error_when_none=False)
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''
            #         item_data['event_link'] = link
            
            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
