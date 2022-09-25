from spider_template import GGVenturesSpider


class Mda0001Spider(GGVenturesSpider):
    name = "mda_0001"
    start_urls = ["https://ase.md/contacte/"]
    country = "Moldova"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Academia de Studii Economice a Moldovei (ASEM)"
    
    static_logo = "https://ase.md/wp-content/uploads/2020/10/logo-asem.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ase.md/category/evenimente/"

    university_contact_info_xpath = "//div[contains(@class,'kingster-with-frame')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
            
            event_times = self.multi_event_dates(date_xpath="//span[contains(@class,'blog-info-date')]")  
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='aktiviti_info']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://ase.md/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    datetime = event_times.pop(0)
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='kingster-single-article-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='kingster-single-article-content']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = datetime
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[text()='Event Summary']/following-sibling::div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[text()='Event Summary']/following-sibling::div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='article-coordination-info']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
