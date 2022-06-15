from spider_template import GGVenturesSpider


class Usa0092Spider(GGVenturesSpider):
    name = 'usa_0092'
    start_urls = ["https://jindal.utdallas.edu/about-the-jindal-school-of-management/contact/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of Texas at Dallas,School of Management"
    
    static_logo = "https://www.collegeconsensus.com/wp-content/uploads/2018/12/online-mba-the-university-of-texas-at-dallas-logo-177178.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://jindal.utdallas.edu/calendar/"

    university_contact_info_xpath = "//div[@id='content']"
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
            for link in self.events_list(event_links_xpath="//h3[@class='event-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://jindal.utdallas.edu/calendar/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='entry-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='detail-description']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='detail-date']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='detail-time']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'detail-event-meta-data')]"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
