from spider_template import GGVenturesSpider


class Chn0043Spider(GGVenturesSpider):
    name = 'chn_0043'
    start_urls = ["https://www.tsinghua.edu.cn/en/Contact.htm"]
    country = 'China'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Tsinghua University"
    
    static_logo = "https://www.tsinghua.edu.cn/en/image/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.tsinghua.edu.cn/en/Events1.htm"

    university_contact_info_xpath = "//div[@id='vsb_content']"
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
            
            raw_event_times = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//section//ul/li//div[@class='date']")))
            event_times = [x.text for x in raw_event_times]
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//section//ul/li/a",next_page_xpath="//a[text()='Next']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//section//ul/li/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.tsinghua.edu.cn/en/info/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    datetime = event_times.pop(0)

                    item_data['event_link'] = link
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h5[@class='tit']"])
                    
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='w84'] | //div[starts-with(@class,'rich_media_content')]"],enable_desc_image=True,error_when_none=False)

                    item_data['event_date'] = datetime.replace("\n","")
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[contains(text(),'Time')]").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)
                    
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
