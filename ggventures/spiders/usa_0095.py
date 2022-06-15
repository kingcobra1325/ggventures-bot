from spider_template import GGVenturesSpider


class Usa0095Spider(GGVenturesSpider):
    name = 'usa_0095'
    start_urls = ["https://thunderbird.asu.edu/about/contact-us"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Thunderbird,Garvin School of International Management"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Thunderbird_School_of_Global_Management_Seal.svg/1200px-Thunderbird_School_of_Global_Management_Seal.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://thunderbird.asu.edu/about/events"

    university_contact_info_xpath = "//div[starts-with(@class,'layout__region')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            self.ClickMore(click_xpath="//a[text()='Load more']",run_script=True)
              
            raw_event_times = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//strong[@class='detail date']/..")))
            event_times = [x.text for x in raw_event_times]
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='col']/h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://na.eventscloud.com/ereg/","https://t-birdconnect.com/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link
                    
                    datetime = event_times.pop(0)

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'header-content-containe')] | //div[@data-testid='event-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//td[@class='standard '] | //div[starts-with(@class,'grid__item')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = datetime
                    item_data['event_time'] = datetime
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'contact')]/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
