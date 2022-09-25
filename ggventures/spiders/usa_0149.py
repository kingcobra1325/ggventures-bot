from spider_template import GGVenturesSpider


class Usa0149Spider(GGVenturesSpider):
    name = 'usa_0149'
    start_urls = ["https://business.wsu.edu/contact/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Washington State University,College of Business"
    
    static_logo = "https://s3.wp.wsu.edu/uploads/sites/609/2017/06/wsu-carson-college-350p.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://business.wsu.edu/news-events/calendar/"

    university_contact_info_xpath = "//div[@id='page-3622']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//li[text()='There were no results found.']")
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[@class='tribe-event-url']",next_page_xpath="//li[@class='tribe-events-nav-next tribe-events-nav-right']/a",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//h3[@class='summary']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://business.wsu.edu/news-events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='tribe-events-single-event-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-single-event-description')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//dd[@class='custom-field-contact_email']/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
