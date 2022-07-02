from spider_template import GGVenturesSpider


class Nzl0003Spider(GGVenturesSpider):
    name = "nzl_0003"
    start_urls = ["https://www.massey.ac.nz/massey/explore/departments/massey-business-school/massey-business-school_home.cfm"]
    country = "New Zealand"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Massey University,College of Business"
    
    static_logo = "https://www.anzam.org/wp-content/uploads/2020/03/Massey-Business-School-Logo-CMYK.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.massey.ac.nz/massey/about-massey/events/events_home.cfm"

    university_contact_info_xpath = "//div[starts-with(@class,'office-contact')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='eur-events-list']//a",next_page_xpath="//a[text()='Next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//h3[@class='event-card__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.massey.ac.nz/about/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='page-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='block-paragraph']",],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event-page__hero-meta-wrapper']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-page__hero-meta-wrapper']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
