from spider_template import GGVenturesSpider


class Mda0001Spider(GGVenturesSpider):
    name = 'mda_0001'
    start_urls = ['https://ase.md/contacte/']
    country = "Moldova"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Academia de Studii Economice a Moldovei (ASEM)"
    static_logo = "https://ase.md/wp-content/uploads/2020/10/logo-asem.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ase.md/category/evenimente/"

    university_contact_info_xpath = "//div[contains(@class,'kingster-with-frame')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@class='post-content']",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False):
                # for link in self.events_list(event_links_xpath="//div[contains(@class,'et_pb_row_4')]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['ase.md']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).text
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//article").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event-desc')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//article").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//article").text

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
