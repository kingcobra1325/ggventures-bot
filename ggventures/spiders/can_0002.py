from spider_template import GGVenturesSpider


class Can0002Spider(GGVenturesSpider):
    name = "can_0002"
    start_urls = ["https://sprott.carleton.ca/contact-us/"]
    country = "Canada"
    # eventbrite_id = 12790629019

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Carleton University,Sprott School of Business"
    
    static_logo = "https://pbs.twimg.com/media/FMNgMxZWUAMuWGU?format=jpg&name=4096x4096"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://sprott.carleton.ca/events/"

    university_contact_info_xpath = "//main[@id='content']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            self.check_website_changed(upcoming_events_xpath="//li[text()='No Items.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2[@class='entry-title']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
#             for link in self.events_list(event_links_xpath="//li[@itemprop='item']/a"):
#                 self.getter.get(link)
#                 if self.unique_event_checker(url_substring=["https://sprott.carleton.ca/event/"]):
                    
#                     self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

#                     item_data = self.item_data_empty.copy()
                    
#                     item_data['event_link'] = link

#                     item_data['event_name'] = self.scrape_xpath(xpath_list=["//section/h1"])
#                     item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='content']","//div[contains(@class,'structured-content-rich-text')]"],enable_desc_image=True,error_when_none=False)
#                     item_data['event_date'] = self.scrape_xpath(xpath_list=["//dt[text()='Start']/following-sibling::dd"],method='attr',error_when_none=False,wait_time=5)
#                     item_data['event_time'] = self.scrape_xpath(xpath_list=["//dt[text()='Time']/following-sibling::dd"],method='attr',error_when_none=False,wait_time=5)
#                     # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# # 
#                     yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
