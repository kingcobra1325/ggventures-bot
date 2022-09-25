from spider_template import GGVenturesSpider


class Deu0030Spider(GGVenturesSpider):
    name = 'deu_0030'
    start_urls = ["https://www.wiwi.uni-passau.de/en/contact/"]
    country = 'Germany'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universität Passau,Passau Graduate School of Business"
    
    static_logo = "https://www.uni-passau.de/typo3conf/ext/upatheme/Resources/Public/img/Logo_zentral_farbig_EN.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uni-passau.de/en/university/about-the-university/university-media/calendar-of-events/?no_cache=1"

    university_contact_info_xpath = "//div[@class='ce-wrapper']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//h2[@class=' default_catheader']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.uni-passau.de/en/university/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2[@class='main']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='csc-textpic-text']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//*[text()='Date & Time']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//*[text()='Date & Time']/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
