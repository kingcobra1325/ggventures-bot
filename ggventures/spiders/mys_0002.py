from spider_template import GGVenturesSpider


class Mys0002Spider(GGVenturesSpider):
    name = "mys_0002"
    start_urls = ["https://sgs.upm.edu.my/contact-3764"]
    country = "Malaysia"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universiti Putra Malaysia (UPM),Graduate School of Management"
    
    static_logo = "https://sgs.upm.edu.my/assets/images/logoupm.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://sgs.upm.edu.my/activities"

    university_contact_info_xpath = "//table"
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='aktiviti_info']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["sgs.upm.edu.my/activities"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[text()='Event Title']/following-sibling::div"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[text()='Event Summary']/following-sibling::div"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[text()='Date']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[text()='Time']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='enquiries-contact']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
