from spider_template import GGVenturesSpider


class Usa0112Spider(GGVenturesSpider):
    name = 'usa_0112'
    start_urls = ["https://www.terry.uga.edu/contact-us"]
    country = 'US'
    # eventbrite_id = 6221361805

    handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Georgia, Terry College of Business"
    
    static_logo = "https://www.terry.uga.edu/themes/custom/gold_terry/img/Screen_TERRY_2_line_Full_Color_White_Text.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://calendar.uga.edu/terry/calendar/month"

    university_contact_info_xpath = "//div[@class='field_two_column_list']"
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[@class='summary']/a",next_page_xpath="//a[@id='next-number']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//a[@class='redirect']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://calendar.uga.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='summary']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='description']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='dateright']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='dateright']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//dt[@class='custom-field-event_contact_name']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
