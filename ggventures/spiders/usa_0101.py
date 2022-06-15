from spider_template import GGVenturesSpider


class Usa0101Spider(GGVenturesSpider):
    name = 'usa_0101'
    start_urls = ["https://ualr.edu/business/contact-us/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Arkansas at Little Rock,College of Business"
    
    static_logo = "https://www.collegeconsensus.com/wp-content/uploads/2018/12/elearning-university-of-arkansas-at-little-rock-logo-130263.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ualr.edu/www/events/"

    university_contact_info_xpath = "//div[@id='main']/div[@id='container']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.element_to_be_clickable((self.Mth.By.XPATH,"//button[@data-view='month']"))).click()
            self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.element_to_be_clickable((self.Mth.By.XPATH,"//li[contains(text(),'List')]"))).click()
            
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[@class='tribe-event-url']",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//h3[@class='event-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://ualr.edu/www/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='tribe-events-single-event-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-single-event-description')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h2[contains(text(),'Organizer')]/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
