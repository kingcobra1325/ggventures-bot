from spider_template import GGVenturesSpider


class Ind0018Spider(GGVenturesSpider):
    name = "ind_0018"
    start_urls = ["https://www.iitb.ac.in/en/about-iit-bombay/contact-us"]
    country = "India"
    # eventbrite_id = 14858065474
# 
    handle_httpstatus_list = [301,302,403,404]

    static_name = "Indian Institute of Technology (IIT) Bombay"
    
    static_logo = "https://www.iitb.ac.in/sites/www.iitb.ac.in/themes/touchm/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.iitb.ac.in/calendar-node-field-event-date"

    university_contact_info_xpath = "//div[@id='content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//span[@class='field-content']/a | //td[@class='multi-day']//a",next_page_xpath="//li[@class='date-next']/a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[@class='media-body']/a[1]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.iitb.ac.in/en/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='page_title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@property='content:encoded']",],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Event Date')]/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Event Date')]/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
