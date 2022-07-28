from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Can0003Spider(GGVenturesSpider):
    name = 'can_0003'
    start_urls = ["https://www.concordia.ca/jmsb/programs/graduate/contact-us.html"]
    country = 'Canada'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Concordia University,John Molson School of Business"
    
    static_logo = "https://icmrindia.org/just-in-case/Newsletter/image/logo6.jpg"

    parse_code_link = "https://www.concordia.ca/events.html"

    university_contact_info_xpath = "//div[@class='rte']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//span[text()='Load More']",final_counter=3)

            for link in self.events_list(event_links_xpath="//a[text()='More info']"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="concordia.ca"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'content-section')]//div[contains(@class,'main')]"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='info']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='info']"],method='attr')
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[contains(text(),'CONTACT')]/following-sibling::p"],error_when_none=False,wait_time=5)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
