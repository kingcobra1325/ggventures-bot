from spider_template import GGVenturesSpider


class Usa0078Spider(GGVenturesSpider):
    name = 'usa_0078'
    start_urls = ["https://eller.arizona.edu/contact"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of Arizona, Eller College of Management"
    
    static_logo = "https://eller.arizona.edu/sites/default/files/Eller_Webheader.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://eller.arizona.edu/news-events/events"

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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='card']/a",next_page_xpath="//a[text()='next ›']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='card']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://eller.arizona.edu/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@id='page-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='content']//div[@class='col-xs-12']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='field-uaqs-date']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='field-uaqs-date']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[contains(text(),'Event Cont')]"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
