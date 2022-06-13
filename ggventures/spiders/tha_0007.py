from spider_template import GGVenturesSpider
from time import sleep

class Tha0007Spider(GGVenturesSpider):
    name = 'tha_0007'
    start_urls = ["https://tu.ac.th/about"]
    country = 'Thailand'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Thammasat University"
    
    static_logo = "https://tu.ac.th/uploads/main-logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://tu.ac.th/calendar/events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True
    # USE_MULTI_DRIVER=True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='listItemWrap']/a",next_page_xpath="//a[@class='nextPage']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            num_of_events = len(self.events_list(event_links_xpath="//a[contains(@class,'more-detail-btn')]",return_elements=True))
            for link in range(0,num_of_events):
                sleep(5)
                self.events_list(event_links_xpath="//a[contains(@class,'more-detail-btn')]",return_elements=True)[link].click()
                if self.unique_event_checker(url_substring=["tu.ac.th/calendar/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = self.getter.current_url
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='title']"],method='attr')

                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='description']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//ul[@class='detail']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//ul[@class='detail']"],method='attr')
                    

                    yield self.load_item(item_data=item_data,item_selector=link)
                self.driver.get(response.url)
        ####################
        except Exception as e:
            self.exception_handler(e)
