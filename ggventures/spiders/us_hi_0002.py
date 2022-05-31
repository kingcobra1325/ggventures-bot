from spider_template import GGVenturesSpider


class UsHi0002Spider(GGVenturesSpider):
    name = 'us-hi_0002'
    start_urls = ['https://shidler.hawaii.edu/contact']
    country = 'Hawaii'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Hawaii at Manoa, Schidler College of Business"
    
    static_logo = "https://clarencelee.com/cld-renew/wp-content/uploads/2016/08/school_id_shidler_01.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://shidler.hawaii.edu/events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h4/a",next_page_xpath="//span[text()='Weiter']/..",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'views-row')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["shidler.hawaii.edu/events"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[contains(@class,'page-title')]"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//article"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//article"])
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//article"])
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Kontakt')]/following-sibling::div"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    


                    yield self.load_item(item_data=item_data,item_selector=link)
        
        ####################
            self.driver.get('https://www.hawaii.edu/calendar/manoa/')
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//td[@class='eventTitle']/a",next_page_xpath="//div[@class='nextMonthDiv']/a",get_next_month=True,click_next_month=False,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//div[contains(@class,'views-row')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["hawaii.edu/calendar/manoa"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='event-display']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='event-display']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='event-display']"],method='attr')
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Kontakt')]/following-sibling::div"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link


                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)