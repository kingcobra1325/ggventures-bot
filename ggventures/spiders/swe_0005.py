from spider_template import GGVenturesSpider


class Swe0005Spider(GGVenturesSpider):
    name = 'swe_0005'
    start_urls = ["https://www.hhs.se/en/about-us/contact/"]
    country = 'Sweden'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Stockholm School of Economics"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Stockholm_School_Of_Economics_Logo.svg/1200px-Stockholm_School_Of_Economics_Logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.hhs.se/en/about-us/calendar/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h1[@class='c-event-list__item__heading']/a",next_page_xpath="//a[@title='next']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//h1[@class='c-event-list__item__heading']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.hhs.se/en/about-us/calendar/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[starts-with(@class,'o-grid__cell')]")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//p[@class='event_date']").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//p[@class='event_date']").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'c-article__info')]/div").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'c-article__info')]/div").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
                    # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
