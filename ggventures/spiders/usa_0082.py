from spider_template import GGVenturesSpider


class Usa0082Spider(GGVenturesSpider):
    name = 'usa_0082'
    start_urls = ["https://michiganross.umich.edu/about/dean-search"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of Michigan, Stephen M. Ross School of Business"
    
    static_logo = "https://wdi-publishing.com/wp-content/uploads/2017/02/RossLogo_Centered_cmyk-1.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://michiganross.umich.edu/about/events/browse-all"

    university_contact_info_xpath = "//body"
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//td[contains(@class,'field-title')]/a",next_page_xpath="//a[text()='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='lw_events_title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://michiganross.umich.edu/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='pane-content']//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'body')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[@class='date-display-start']/.."],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[@class='date-display-start']/.."],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='contact']"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
