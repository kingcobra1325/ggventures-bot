from spider_template import GGVenturesSpider


class Arg0003Spider(GGVenturesSpider):
    name = 'arg_0003'
    start_urls = ["https://www.itba.edu.ar/contactate/"]
    country = "Argentina"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "ITBA - Instituto Tecnologico de Buenos Aires"
    
    static_logo = "https://www.itba.edu.ar/wp-content/uploads/2021/08/ITBA-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.itba.edu.ar/agenda-new/"

    university_contact_info_xpath = "//h5[text()='Contacto']/.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//span[@class='fc-calendar-title']/a",next_page_xpath="//span[@class='fc-icon fc-icon-chevron-right']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//h5[@class='mb-3']/following-sibling::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.itba.edu.ar/agenda/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='tribe-events-single-event-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-single-event-description')]"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[text()='Event contact details']/following-sibling::ul"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
