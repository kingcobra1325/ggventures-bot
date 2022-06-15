from spider_template import GGVenturesSpider


class Usa0084Spider(GGVenturesSpider):
    name = 'usa_0084'
    start_urls = ["https://www.unm.edu/contactunm.html"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of New Mexico, The Anderson School of Management"
    
    static_logo = "https://www.mgt.unm.edu/video/unmanderson-logo-large.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.mgt.unm.edu/events/default.asp?main=events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='eventHeader']/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://events.uiowa.edu/"]):
            
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//li[@class='eventFullItem']"):
                    
                self.Func.print_log(f"Currently scraping --> {self.driver.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = self.driver.current_url
                
                item_data['event_name'] = link.find_element(self.Mth.By.XPATH,".//div[@class='eventFullTitleBox']").text
                item_data['event_desc'] = link.find_element(self.Mth.By.XPATH,".//div[@class='eventFullDescBox']").text
                item_data['event_date'] = link.find_element(self.Mth.By.XPATH,".//div[@class='eventFullDateBox']").text
                item_data['event_time'] = link.find_element(self.Mth.By.XPATH,".//div[@class='eventFullDateBox']").text
                
                # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//a[@id='contactName']/ancestor::div[1]"],method='attr',error_when_none=False)
                # item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"],driver=link)
                # item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='description']"],enable_desc_image=True,error_when_none=False)
                # item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='date']"],method='attr',error_when_none=False)
                # item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='time']"],method='attr',error_when_none=False)
                # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//a[@id='contactName']/ancestor::div[1]"],method='attr',error_when_none=False)

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
