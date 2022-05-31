from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Fra0005Spider(GGVenturesSpider):
    name = 'fra_0005'
    start_urls = ['https://www.edhec.edu/en/contact-us']
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "EDHEC Business School"
    static_logo = "https://thumbnail.imgbin.com/4/10/1/imgbin-edhec-business-school-logo-brand-product-design-font-design-GAgCLtthhn0Xb2mxBV1zHnkq4_t.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://www.edhec.edu/en/evenements'

    university_contact_info_xpath = "//div[contains(@id,'block-system-main')]"
    contact_info_text = True
    # contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//h2[contains(@class,'not-found-title')]")

            for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[contains(@class,'dexp-grid-item')]//a",next_page_xpath="//span[contains(@class,'next-month')]/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//div[contains(@class,'sk-allevents')]/a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=['www.edhec.edu/en/agenda']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'field-type-text-with-summary')]"],method='attr',error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='date-zone']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'date-heure')]"],method='attr',error_when_none=False)
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[contains(text(),'CONTACT')]/following-sibling::p"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
