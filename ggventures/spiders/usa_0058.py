from spider_template import GGVenturesSpider


class Usa0058Spider(GGVenturesSpider):
    name = 'usa_0058'
    start_urls = ["https://dotcio.rpi.edu/get-help"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Rensselaer Polytechnic Institute,Lally School of Management and Technology"
    
    static_logo = "https://lallyschool.rpi.edu/themes/custom/papiermache/img/RPI-Web-Logo-White@2x.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://lallyschool.rpi.edu/news"

    university_contact_info_xpath = "//div[@class='field__item'][2]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'events-container')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://events.rpi.edu/cal/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2[contains(@class,'eventTitle')]"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='eventDescription']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='eventWhen']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='eventWhen']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='eventContact']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)

