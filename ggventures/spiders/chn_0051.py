from spider_template import GGVenturesSpider


class Chn0051Spider(GGVenturesSpider):
    name = "chn_0051"
    start_urls = ["http://english.zjgsu.edu.cn/list-51.html"]
    country = "China"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Zhejiang Gongshang University (ZJGSU)"
    
    static_logo = "http://english.zjgsu.edu.cn/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "http://english.zjgsu.edu.cn/List-58.html"

    university_contact_info_xpath = "//div[@class='col-right']"
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'list_events')]/a",next_page_xpath="//a[text()='Next']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='r_content']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["http://english.zjgsu.edu.cn/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h5"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'r_content')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'r_content')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'r_content')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
