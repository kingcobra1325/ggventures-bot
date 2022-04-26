from spider_template import GGVenturesSpider


class Ltu0003Spider(GGVenturesSpider):
    name = 'ltu_0003'
    start_urls = ['https://www.ism.lt/en/contacts/']
    country = "Lithuania"
    # eventbrite_id = 6552000185
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "ISM University of Management & Economics"
    static_logo = "https://www.ism.lt/wp-content/uploads/2021/01/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ism.lt/en/news-and-events/"

    university_contact_info_xpath = "//div[contains(@class,'contact-card-padding')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='tab-upcoming']",empty_text=True)
            self.ClickMore(click_xpath="//button[@class='load-more-ne-btn']",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[contains(@class,'listing')]/div/a",next_page_xpath="//li[@class='next']/a",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='grid']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.ism.lt/en']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[contains(@class,'wpb_text_column')]"))).text
                    try:
                        item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[contains(@class,'event-news-title')]"))).text
                        item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='news-content']").text
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='news-content']").text
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='news-content']").text
                    except (self.Exc.TimeoutException,self.Exc.NoSuchElementException) as e:
                        self.Func.print_log(f"XPATH not found {e}: Using Alternate Xpath...",'debug')
                        item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[contains(@class,'wpb_text_column')]"))).text
                        item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'mb-3 pb-2')]//div[contains(@class,'wpb_text_column')]").text
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'mb-3 pb-2')]//div[contains(@class,'wpb_text_column')]").text
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'mb-3 pb-2')]//div[contains(@class,'wpb_text_column')]").text
                    # item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'mb-3 pb-2')]//div[contains(@class,'wpb_text_column')]").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event-desc')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'mb-3 pb-2')]//div[contains(@class,'wpb_text_column')]").text
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'mb-3 pb-2')]//div[contains(@class,'wpb_text_column')]").text

                    # item_data['event_date'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",'content')
                    # item_data['event_time'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",'content')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....","debug")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(text(),'Contact')]/parent::li").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
