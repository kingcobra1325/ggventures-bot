from spider_template import GGVenturesSpider


class Pol0003Spider(GGVenturesSpider):
    name = "pol_0003"
    start_urls = ["https://www.kozminski.edu.pl/en/contact"]
    country = "Poland"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "LKAEM - Leon Kozminski Academy of Entrepreneurship and Management"
    
    static_logo = "https://studyqa.com/media/upload/univers/934/05/uni_profile_93405.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.kozminski.edu.pl/en/events"

    university_contact_info_xpath = "//section[contains(@class,'block-field-paragraphs')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='eur-events-list']//a",next_page_xpath="//a[text()='Next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'button-wrapper')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["kozminski.edu.pl/en/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'body')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[contains(@class,'date')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='body']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
