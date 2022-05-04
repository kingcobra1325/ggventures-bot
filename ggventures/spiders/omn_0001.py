from spider_template import GGVenturesSpider

class Omn0001Spider(GGVenturesSpider):
    name = 'omn_0001'
    start_urls = ['https://www.squ.edu.om/economics/']
    country = "Oman"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Sultan Qaboos University,College of Commerce and Economics"
    static_logo = "https://res.cloudinary.com/climb/image/upload/c_fill,f_auto,h_250,w_250,q_80/v1523928499/hh0txrdz9ti35dectkof"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.nhh.no/en/calendar/"

    university_contact_info_xpath = "//main"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='events-items']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//li[@class='activity-item']/a",next_page_xpath="//li[@aria-label='Next page']",click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//a[@class='eventLink']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.nhh.no/en/calendar']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1/span[@class='textMega']"))).get_attribute('textContent')
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='pageBoundary']").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event-desc')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='activity-page__day--start']").text
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='activity-page__day--start']").text

                    item_data['event_date'] = self.get_datetime_attributes("//time[@class='eventDate']",'datetime')
                    item_data['event_time'] = self.get_datetime_attributes("//time[@class='eventDate']",'datetime')

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
