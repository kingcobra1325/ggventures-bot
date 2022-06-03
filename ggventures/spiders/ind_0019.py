from spider_template import GGVenturesSpider


class Ind0019Spider(GGVenturesSpider):
    name = 'ind_0019'
    start_urls = ["https://home.iitd.ac.in/contact.php"]
    country = 'India'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Indian Institute of Technology (IIT) Delhi"
    
    static_logo = "https://home.iitd.ac.in/images/logo-iit.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://home.iitd.ac.in/index.php"

    university_contact_info_xpath = "//section[starts-with(@class,'divider')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.alert_handler(alert_driver=self.driver,alert_text='Abort',alert_accept=False)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h4/a",next_page_xpath="//span[text()='Weiter']/..",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[@class='info']//a"):
                self.getter.get(link)
                
                self.alert_handler(alert_driver=self.getter,alert_text='Cancel',alert_accept=False)
                if self.unique_event_checker(url_substring=["https://home.iitd.ac.in/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2[@class='title']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='section-title']/following-sibling::div")

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='section-title']/following-sibling::div").get_attribute('textContent')
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='section-title']/following-sibling::div").get_attribute('textContent')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'tribe-events-schedule')]").get_attribute('textContent')
                    #     # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='elementObjectEventMultiTime']").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
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
