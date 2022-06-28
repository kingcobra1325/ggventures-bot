from spider_template import GGVenturesSpider


class Deu0035Spider(GGVenturesSpider):
    name = "deu_0035"
    start_urls = ["https://www.whu.edu/en/footernavigation/contact-us/"]
    country = "Germany"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "WHU Vallendar,Otto Beisheim School of Management"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/WHU_Logo.svg/1200px-WHU_Logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.whu.edu/en/events/"

    university_contact_info_xpath = "//footer/div"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='card-header']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.whu.edu/de/konferenzen/","https://events.blackthorn.io/en/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[starts-with(@class,'event-name')] | //h1[@class=' lightblue']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//main",],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'start-date')]/.. | //h2[contains(@class,'darkblue')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'start-date')]/.. | //h2[contains(@class,'darkblue')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
