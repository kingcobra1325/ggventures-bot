from spider_template import GGVenturesSpider


class Swe0005Spider(GGVenturesSpider):
    name = "swe_0005"
    start_urls = ["https://www.hhs.se/en/about-us/contact/"]
    country = "Sweden"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Stockholm School of Economics"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Stockholm_School_Of_Economics_Logo.svg/1200px-Stockholm_School_Of_Economics_Logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.hhs.se/en/about-us/calendar/"

    university_contact_info_xpath = "//article[@id='article']"
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h1[@class='c-event-list__item__heading']/a",next_page_xpath="//a[@title='next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[contains(@class,'button-wrapper')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.hhs.se/en/about-us/calendar/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'o-grid__cell')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'c-article__info')]/div"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'c-article__info')]/div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
