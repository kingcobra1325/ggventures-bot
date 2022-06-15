from spider_template import GGVenturesSpider


class Usa0102Spider(GGVenturesSpider):
    name = 'usa_0102'
    start_urls = ["https://haas.berkeley.edu/about/contact/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of California - Berkeley, Haas School of Business"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Berkeley-Haas_School_of_Business_Logo.svg/2560px-Berkeley-Haas_School_of_Business_Logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://haas.berkeley.edu/event"

    university_contact_info_xpath = "//section[starts-with(@class,'entry-content')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[@class='tribe-event-url']",next_page_xpath="(//span[text()='Next Events'])[2]",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//a[@class='tribe-event-url']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://haas.berkeley.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[starts-with(@class,'tribe-events-single-event-title')]"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-single-event-description')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='tribe-event-schedule']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='tribe-event-schedule']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'detail-event-meta-data')]"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
