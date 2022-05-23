from spider_template import GGVenturesSpider


class Usa0018Spider(GGVenturesSpider):
    name = 'usa_0018'
    start_urls = ["https://mason.wm.edu/contact/index.php"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "College of William and Mary,Mason School of Business"
    
    static_logo = "https://mason.wm.edu/img/wm_business_vertical_full_color.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://events.wm.edu/calendar/upcoming/mason"

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
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[@class='event__url']",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='event_grid_item']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://events.wm.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='event_longdesc']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='event_datetime']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='event_datetime']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@id='event_contact']"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
