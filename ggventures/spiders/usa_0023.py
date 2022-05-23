from spider_template import GGVenturesSpider


class Usa0023Spider(GGVenturesSpider):
    name = 'usa_0023'
    start_urls = ["https://www.depaul.edu/Pages/contact-us.aspx"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "DePaul University,College of Commerce & Kellstadt Graduate School of Business"
    
    static_logo = "https://scontent.fmnl17-3.fna.fbcdn.net/v/t39.30808-6/273303476_10159046001029576_6558481039033534096_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeG6ME2aTt4R6KtO6kZoi-mziXUy9YbXsgWJdTL1hteyBWg-T3MYZ60zrQQRMOjiDD8OOEV4XAiU42lZYIWuHNje&_nc_ohc=AE7y6f6dpVkAX8MlNEU&_nc_ht=scontent.fmnl17-3.fna&oh=00_AT-0WEy1D4nvfBo79jfA4EExXV7zkfyoy9ZnFados2959Q&oe=6290A885"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://business.depaul.edu/news-events/events/Pages/default.aspx"

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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='events-card']/a",next_page_xpath="//span[text()='Next Page']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='lw_event_item_title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://events.depaul.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='description']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='dateright']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='dateright']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[text()='Contact Info']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
