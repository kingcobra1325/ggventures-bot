from spider_template import GGVenturesSpider

class Ken0002Spider(GGVenturesSpider):
    name = 'ken_0002'
    start_urls = ['https://sbs.strathmore.edu/contact/']
    country = "Kenya"
    # eventbrite_id = 6552000185
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Strathmore Business School"
    static_logo = "https://sbs.strathmore.edu/wp-content/uploads/2020/10/sbs_logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://sbs.strathmore.edu/events/"

    university_contact_info_xpath = "//div[contains(@class,'fusion-text-1')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(text(),'no item that match')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//tr[@class='single-day']//td//a",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False):
            for link in self.events_list(event_links_xpath="//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['strathmore.edu/event']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2"))).text
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'tribe-events-single-event-description')]").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'text-with-summary')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//h3").get_attribute('textContent')
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//h3").get_attribute('textContent')

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
                        item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//dd[@class='tribe-organizer-tel']").text
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)