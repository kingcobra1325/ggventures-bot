from spider_template import GGVenturesSpider


class Ind0018Spider(GGVenturesSpider):
    name = 'ind_0018'
    start_urls = ["https://www.iitb.ac.in/en/about-iit-bombay/contact-us"]
    country = 'India'
    # eventbrite_id = 6221361805

    handle_httpstatus_list = [301,302,403,404]

    static_name = "Indian Institute of Technology (IIT) Bombay"
    
    static_logo = "https://www.iitb.ac.in/sites/www.iitb.ac.in/themes/touchm/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.iitb.ac.in/calendar-node-field-event-date"

    university_contact_info_xpath = "//div[@id='content']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//span[@class='field-content']/a | //td[@class='multi-day']//a",next_page_xpath="//li[@class='date-next']/a",get_next_month=True,click_next_month=False,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//h2[starts-with(@class,'node__title')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.iitb.ac.in/en/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='page_title']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='content']").get_attribute("textContent")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                    #self.getter.find_element(self.Mth.By.XPATh,"//span[@class='date-display-range']/span")
                    try:
                        item_data['event_date'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",datetime_attribute="content")
                        item_data['event_time'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",datetime_attribute="content")
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # logger.debug(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(text(),'Kontakt')]/following-sibling::div").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
