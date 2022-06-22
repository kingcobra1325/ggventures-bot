from spider_template import GGVenturesSpider


class Chn0038Spider(GGVenturesSpider):
    name = "chn_0038"
    start_urls = ["https://e.swufe.edu.cn/ABOUT/CONTACT_US.htm"]
    country = "China"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Southwest University of Finance and Economics (SWUFE)"
    
    static_logo = "https://e.swufe.edu.cn/dfiles/9861/eswufe/english/images/1_02.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://e.swufe.edu.cn/NEWS___EVENTS/EVENTS.htm"

    university_contact_info_xpath = "//div[@class='left_content']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2[@class='card-title']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='events1']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://e.swufe.edu.cn/info/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h4"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='vsb_content']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[text()='Time']/ancestor::p | //span[text()='Time：']/ancestor::p[starts-with(@style,'line-height')]/following-sibling::p | //span[text()='Time：']/ancestor::p[starts-with(@style,'text-align')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[text()='Time']/ancestor::p | //span[text()='Time：']/ancestor::p[starts-with(@style,'line-height')]/following-sibling::p | //span[text()='Time：']/ancestor::p[starts-with(@style,'text-align')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
