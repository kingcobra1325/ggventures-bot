from spider_template import GGVenturesSpider


class Usa0087Spider(GGVenturesSpider):
    name = 'usa_0087'
    start_urls = ["https://business.und.edu/about/contact-us/index.html"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of North Dakota, College of Business & Public Administration"
    
    static_logo = "https://blogs.und.edu/cobpa/wp-content/uploads/sites/87/2020/02/Nistler-Logo-Blog-Header-450x300.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://calendar.und.edu/calendar"

    university_contact_info_xpath = "//div[starts-with(@class,'main__content')]"
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[@class='emu-card_title-link']",next_page_xpath="//a[@class='em-pagination-item arrow']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='eventHeader']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://calendar.und.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='em-header-card_title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='em-content_about']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='em-list_dates__container']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='time']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[text()='Contact Email']/ancestor::div[@class='em-event-meta-data-container']"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
