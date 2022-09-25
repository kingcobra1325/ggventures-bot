from spider_template import GGVenturesSpider


class Aus0026Spider(GGVenturesSpider):
    name = 'aus_0026'
    start_urls = ["https://business.uq.edu.au/contact"]
    country = "Australia"
    eventbrite_id = 31577513049

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Queensland,UQ Business School (Brisbane Graduate School of Business)"
    
    static_logo = "https://images.squarespace-cdn.com/content/v1/5bb947c88d97400df83137ac/1585011292636-9EI1CGQ7GA7Q5IMQPXKE/BusinessSchool-SponsSmall-col-rgb.png?format=1000w"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://business.uq.edu.au/events"
    
    USE_FF_DRIVER = True

    university_contact_info_xpath = "//strong[text()='Opening Hours']/../.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@id='qt-event_tabs-foundation-tabs-1']//h3[@Class='event-session__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://business.uq.edu.au/event/","ventures.uq.edu.au"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='panel-pane__content']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='content']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[@class='date--start']/.."],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[@class='date--start']/.."],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h5[text()='Contact']/following-sibling::*"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

            
            self.driver.get("https://ventures.uq.edu.au/events")
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@id='qt-event_tabs-foundation-tabs-1']//h3[@Class='event-session__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["ventures.uq.edu.au/event","ventures.uq.edu.au"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='panel-pane__content']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["(//div[@class='row']/div[starts-with(@class,'layout-region__main')])[2]","//div[@class='layout-region__column-one columns medium-6']","//div[@class='layout-region__main large-8 columns']"],enable_desc_image=True,wait_time=30)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[@class='date--start']/..","//span[contains(@class,'icon-calendar')]/.."],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[@class='date--start']/..","//div[@class='content']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h5[text()='Contact']/following-sibling::*"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
