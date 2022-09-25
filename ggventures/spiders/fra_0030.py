from spider_template import GGVenturesSpider


class Fra0030Spider(GGVenturesSpider):
    name = "fra_0030"
    start_urls = ["https://www.insead.edu/get-in-touch"]
    country = "France"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "INSEAD"
    
    static_logo = "https://www.insead.edu/sites/all/themes/insead_theme/img/logo_roundel.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.insead.edu/events"

    university_contact_info_xpath = "//div[@class='container-fluid']"
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
            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'widgetbox')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.insead.edu/centres/","https://www.insead.edu/events/","https://www.insead.edu/conversations/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='heading3']","//h2[@class='text-center']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@role='tabpanel']","//div[@class='panel-separator']/following-sibling::div"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='events-details-info']","//h3[@class='text-center']/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@role='tabpanel']","//div[@class='panel-separator']/following-sibling::div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//th[text()='Contact person:']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
