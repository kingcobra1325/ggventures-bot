from spider_template import GGVenturesSpider


class Fin0004Spider(GGVenturesSpider):
    name = "fin_0004"
    start_urls = ["https://www.utu.fi/en/university/contact-information"]
    country = "Finland"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Turku School of Economics"
    
    static_logo = "https://www.ercis.org/sites/ercis/files/structure/network/partners/turku.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.utu.fi/en/event-search"

    university_contact_info_xpath = "//div[contains(@class,'region--content')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//button[starts-with(@class,'fusion-load-more-button')]",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[contains(@rel,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[@class='fusion-events-wrapper']//h2/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["www.utu.fi/en/news/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1/span"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event__body')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event__time-value')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event__time-value')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//th[text()='Contact person:']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
