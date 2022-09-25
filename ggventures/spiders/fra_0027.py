from spider_template import GGVenturesSpider


class Fra0027Spider(GGVenturesSpider):
    name = "fra_0027"
    start_urls = ["https://www.hec.edu/en/master-s-programs/contact"]
    country = "France"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "HEC School of Management - Paris"
    
    static_logo = "https://www.hec.edu/themes/custom/hec_theme/logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.hec.edu/en/events"

    university_contact_info_xpath = "//div[@class='blocks-list']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            self.ClickMore(click_xpath="//li[contains(@class,'more-button')]",run_script=False)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//th[@class='next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='event-item__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.hec.edu/en/news-room"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1/span"],wait_time=30)
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='rte']"],method='attr',enable_desc_image=False,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event-item__date']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-item__icon']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
