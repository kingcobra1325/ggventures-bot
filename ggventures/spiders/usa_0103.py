from spider_template import GGVenturesSpider


class Usa0103Spider(GGVenturesSpider):
    name = 'usa_0103'
    start_urls = ["https://gsm.ucdavis.edu/contact-us-today#no-back"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of California - Davis,Graduate School of Management"
    
    static_logo = "https://mbatube.com/themes/mbatube/logos/86e54d3e6b2912e52e23432fa98e1f131568703243.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://gsm.ucdavis.edu/calendar"

    university_contact_info_xpath = "//div[@class='page-sidebar--inner']"
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//a[@class='redirect']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://gsm.ucdavis.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='node-content']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event-dates')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event-dates')]"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'email-addresses')]"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
