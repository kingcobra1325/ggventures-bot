from spider_template import GGVenturesSpider


class Cyp0001Spider(GGVenturesSpider):
    name = "cyp_0001"
    start_urls = ["https://www.ciim.ac.cy/contact/"]
    country = "Cyprus"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Cyprus International Institute of Management (CIIM)"
    
    static_logo = "https://www.ciim.ac.cy/wp-content/uploads/2021/10/ciim_logo_tr-o365.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ciim.ac.cy/"

    university_contact_info_xpath = "//section[contains(@id,'custom_html-4')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            self.ClickMore(click_xpath="//button[starts-with(@class,'fusion-load-more-button')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'list_events')]/a",next_page_xpath="//a[text()='Next']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='fusion-events-wrapper']//h2/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.ciim.ac.cy/seminar-series/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-single-event-description')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//dt[@class='tribe-events-start-date-label']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//dt[@class='tribe-events-start-date-label']/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
