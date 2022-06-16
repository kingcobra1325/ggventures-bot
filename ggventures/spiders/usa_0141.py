from spider_template import GGVenturesSpider


class Usa0141Spider(GGVenturesSpider):
    name = 'usa_0141'
    start_urls = ["https://www.darden.virginia.edu/about/contact-us"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Virginia,Darden School of Business"
    
    static_logo = "https://www.darden.virginia.edu/themes/custom/darden_main/images/logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.darden.virginia.edu/events"

    university_contact_info_xpath = "//main//div[starts-with(@class,'clearfix')]"
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='node__content']/a",next_page_xpath="//a[@title='Go to next page']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//h3[@class='summary']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://apply.darden.virginia.edu/register/","https://darden.imodules.com/","https://connect.darden.virginia.edu/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='form_description'] | //div[@class='imod_eventDescription'] | //div[@class='intro-section-container']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@id='register_date'] | //div[@class='imod_eventDate'] | //p[@class='form-paragraph']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@id='register_date'] | //div[@class='imod_eventDate'] | //p[@class='form-paragraph']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='UVA-event-col-right']"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
