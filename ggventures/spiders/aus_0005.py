from spider_template import GGVenturesSpider


class Aus0005Spider(GGVenturesSpider):
    name = 'aus_0005'
    start_urls = ["https://study.csu.edu.au/courses/business"]
    country = 'Australia'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Charles Sturt University,School of International Business"
    
    static_logo = "https://cdn.csu.edu.au/__data/assets/file/0009/2823219/CSU_Logo_01.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://about.csu.edu.au/community/events"

    university_contact_info_xpath = "//div[@class='enquiries desktop-only']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//section[@aria-label='Events']//div[starts-with(@class,'card-content')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://about.csu.edu.au/community/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//a[@id='maincontent']/following-sibling::div"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@Class='date']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@Class='date']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[text()='Contact']/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
