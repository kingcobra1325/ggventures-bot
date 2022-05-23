from spider_template import GGVenturesSpider


class Usa0016Spider(GGVenturesSpider):
    name = 'usa_0016'
    start_urls = ["https://www.cgu.edu/school/drucker-school-of-management/about/staff/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Claremont Graduate University,Peter F. Drucker and Masatoshi Ito Graduate School of Management"
    
    static_logo = "https://www.cgu.edu/wp-content/themes/cgu/assets/images/emblem.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.cgu.edu/events/"

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
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
            
            self.driver.find_element(self.Mth.By.XPATH,"//li[@class='school-drucker-school-of-management']").click()
            self.Func.sleep(3)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[@class='event__url']",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[@class='calendarEvent']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.cgu.edu/event/drucker-school-of-management","https://www.cgu.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='h2']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='u-span-8']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//h5[text()='Date & Time']/following-sibling::p"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//h5[text()='Date & Time']/following-sibling::p"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[text()='Organizer']/following-sibling::div"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
