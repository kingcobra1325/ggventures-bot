from spider_template import GGVenturesSpider


class Chn0042Spider(GGVenturesSpider):
    name = "chn_0042"
    start_urls = ["https://www.tongji.edu.cn/"]
    country = "China"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Tongji University"
    
    static_logo = "https://en.tongji.edu.cn/images/t_logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://en.tongji.edu.cn/event.jsp?urltype=tree.TreeTempUrl&wbtreeid=1004"

    university_contact_info_xpath = "//p[@class='address']/.."
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'list_events')]/a",next_page_xpath="//a[text()='Next']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//ul[starts-with(@class,'events')]/li/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://en.tongji.edu.cn/eventslecture.jsp","https://mp.weixin.qq.com/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'lec_hd')]//h3 | //h1[@class='rich_media_title ']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'lec_main')] | //div[starts-with(@class,'rich_media_content')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'lec_main')] | //div[starts-with(@class,'rich_media_content')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'lec_main')] | //div[starts-with(@class,'rich_media_content')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
