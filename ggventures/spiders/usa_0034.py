from spider_template import GGVenturesSpider


class Usa0034Spider(GGVenturesSpider):
    name = 'usa_0034'
    start_urls = ["https://www.hbs.edu/about/Pages/contact.aspx"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Harvard Business School (HBS)"
    
    static_logo = "https://identity.hbs.edu/wp-content/uploads/2021/09/HBS-styleguide-primary-logo.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.alumni.hbs.edu/events/Pages/default.aspx"

    university_contact_info_xpath = "//div[contains(@class,'contact-us-boxes')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            self.ClickMore(click_xpath="//a[@title='Load More Results']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='events-card']/a",next_page_xpath="//span[text()='Next Page']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//h4/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.alumni.hbs.edu/events/","https://www.exed.hbs.edu/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='gamma-uc']","//h1/span"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='media-body']","//div[@class='sectioned']"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[@class='event-date']","//span[@class='kappa']/.."],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[@class='event-date']","//span[@class='kappa']/.."],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[text()='Contact Info']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
