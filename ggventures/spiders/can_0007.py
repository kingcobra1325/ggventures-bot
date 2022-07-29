from spider_template import GGVenturesSpider


class Can0007Spider(GGVenturesSpider):
    name = "can_0007"
    start_urls = ["https://www.degroote.mcmaster.ca/contact/"]
    country = "Canada"
    # eventbrite_id = 12790629019

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "McMaster University,Michael G. DeGroote School of Business"
    
    static_logo = "https://www.degroote.mcmaster.ca/wp-content/themes/degroote/assets/mcmaster-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.degroote.mcmaster.ca/calendar"

    university_contact_info_xpath = "//div[@class='main-content']//div[@class='container-fluid']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='Sorry, no events found.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
              
#             for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2[@class='card-title']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//h2[@class='card-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://execed.degroote.mcmaster.ca/","https://www.degroote.mcmaster.ca/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='left-col-wide']","//h2[text()='Description']/.."],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='dsb-offering']","//h3[text()='Date & Time']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='dsb-offering']","//h3[text()='Date & Time']/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
