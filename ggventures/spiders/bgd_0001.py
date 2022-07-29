from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Bgd0001Spider(GGVenturesSpider):
    name = 'bgd_0001'
    start_urls = ['http://www.northsouth.edu/academic/sbe/']
    country = "Bangladesh"
    # eventbrite_id = 30819498834

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "North South University,School of Business"
    static_logo = "http://www.northsouth.edu/newassets/images/nsu-photo/logo-4.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "http://www.northsouth.edu/upcoming-events/"

    university_contact_info_xpath = "//div[contains(@class,'container')]//div[@class='col-md-6']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'events')]",empty_text=True)
            # # self.ClickMore(click_xpath="//a[contains(@class,'load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h2/a",next_page_xpath="//a[contains(@aria-label,'next month')]",get_next_month=True,click_next_month=True,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[@class='post-scroller-item']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["http://www.northsouth.edu/upcoming-events/"]):
            
                    logger.info(f"Currently scraping --> {self.getter.current_url}")
            
                    item_data = self.item_data_empty.copy()
            
                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//*[text()='Event Title']/../following-sibling::td"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Details')]/../following-sibling::td"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//*[text()='Date & Time']/../following-sibling::td"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//*[text()='Date & Time']/../following-sibling::td"],method='attr')
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[contains(@class,'fa-whatsapp')]/parent::div"],error_when_none=False,method='attr')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link
            
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
