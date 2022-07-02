from spider_template import GGVenturesSpider

class Irl0004Spider(GGVenturesSpider):
    name = 'irl_0004'
    start_urls = ['https://www.ucc.ie/en/contact/']
    country = "Ireland"
    # eventbrite_id = 6552000185
    # TRANSLATE = True

    handle_httpstatus_list = [301,302,403,404]

    static_name = "University College Cork"
    static_logo = "https://www.ucc.ie/en/media/2017siteassets/images/Logo_easter.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ucc.ie/en/events/"

    university_contact_info_xpath = "//div[contains(@class,'content-wrap__wrapper')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(text(),'No News & Events Foun')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//a[@class='article-list__inner']",next_page_xpath="//span[text()='Next']/parent::a",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//table[@class='eventlist']//p[@class='calendarDescription']/preceding-sibling::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.ucc.ie/en']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2/span"))).get_attribute('textContent')
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='whatsonevent']").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event__body')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     # self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='event__description']").text

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='table_text']").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='table_text']").text

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

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[contains(text(),'Contact')]/parent::td/following-sibling::td").text
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
