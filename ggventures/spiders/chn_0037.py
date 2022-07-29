from spider_template import GGVenturesSpider


class Chn0037Spider(GGVenturesSpider):
    name = 'chn_0037'
    start_urls = ["https://rsc.seu.edu.cn/rsc_en/22018/list.htm"]
    country = 'China'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Southeast University"
    
    static_logo = "https://www.seu.edu.cn/_upload/tpl/0a/5d/2653/template2653/images/logo_sss.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.seu.edu.cn/english/wvents/list.htm"

    university_contact_info_xpath = "//div[@class='wp_entry']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//article[starts-with(@class,'col-md-12')]/h2/a",next_page_xpath="//tr[@class='calendar-box-header']/th[3]/a",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='news_title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.seu.edu.cn/english/","https://cyber.seu.edu.cn/","https://ee.seu.edu.cn/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='entry']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[contains(text(),'会议时间')] | //span[contains(text(),'报告时间：')]/../../.. | //*[starts-with(text(),'Time')]/ancestor::p | //*[starts-with(text(),'When:')]/ancestor::p"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[contains(text(),'会议时间')] | //span[contains(text(),'报告时间：')]/../../.. | //*[starts-with(text(),'Time')]/ancestor::p | //*[starts-with(text(),'When:')]/ancestor::p"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
