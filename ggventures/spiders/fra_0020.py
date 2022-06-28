from spider_template import GGVenturesSpider


class Fra0020Spider(GGVenturesSpider):
    name = "fra_0020"
    start_urls = ["https://www.esdes.fr/en/contact-us/"]
    country = "France"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "ESDES"
    
    static_logo = "https://www.esdes.fr/wp-content/uploads/sites/12/2020/05/logo-esdes-ucly_blanc-website-5.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.esdes.fr/en/welcome/about-esdes/newsroom/all-the-events/"

    university_contact_info_xpath = "//div[@class='page-main']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//button[starts-with(@class,'fusion-load-more-button')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[contains(@rel,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='content-event-image-wrapper']/.."):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.esdes.fr/en/welcome/about-esdes/newsroom"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='page-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'page-content')]","//div[@class='nd-hide-900']/.."],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'single-event-dates')]","//h5[@id='lw_cal_this_day']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'single-event-dates')]","//span[@class='lw_start_time']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
