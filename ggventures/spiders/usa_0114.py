from spider_template import GGVenturesSpider
from datetime import datetime, timedelta
import json
import requests

class Usa0114Spider(GGVenturesSpider):
    name = 'usa_0114'
    start_urls = ["https://www.uidaho.edu/cbe/about/contact-us"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Idaho,College of Business and Economics"
    
    static_logo = "https://www.uidaho.edu/-/media/UIdaho-Responsive/Images/brand-resource-center/toolkit/logo-suites/ui-main-vertical.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uidaho.edu/events"

    university_contact_info_xpath = "//div[starts-with(@class,'obj-sixtysix-thirtythree')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            self.Func.sleep()
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
            self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,'//iframe[contains(@title,"Classic Table Calendar View")]')))
            # self.switch_iframe('//iframe[contains(@title,"Classic Table Calendar View")]',iframe_driver=self.driver)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//article[@class='event-item-list']/a",next_page_xpath="//a[@class='page-link next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//span[@class='twDescription']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["www.uidaho.edu/events"]):
                    self.Func.sleep()
                    # self.switch_iframe('//iframe[contains(@title,"Event Detail")]')
                    self.Mth.WebDriverWait(self.getter, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,'//iframe[contains(@title,"Event Detail")]')))

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@id='headerDiv']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//span[text()='Details']/parent::th/following-sibling::td"],method='attr',enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[text()='When']/parent::th/following-sibling::td"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[text()='When']/parent::th/following-sibling::td"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[contains(text(),'Contact:')]"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
