from spider_template import GGVenturesSpider


class Usa0073Spider(GGVenturesSpider):
    name = 'usa_0073'
    start_urls = ["https://www.fox.temple.edu/contact-us/"]
    country = 'US'
    eventbrite_id = 29609418151

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Temple University,Fox School of Business and Management"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/The_logo_of_Temple_Fox_School_of_Business.jpg/500px-The_logo_of_Temple_Fox_School_of_Business.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.fox.temple.edu/events/"

    university_contact_info_xpath = "//div[@class='col-md-8']"
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='events-card']/a",next_page_xpath="//span[text()='Next Page']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//a[contains(@class,'card-preview__permalink')]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["fox.temple.edu/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='event--content']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event-meta']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-meta']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[text()='Contact Info']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
