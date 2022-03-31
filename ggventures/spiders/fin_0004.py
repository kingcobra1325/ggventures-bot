from spider_template import GGVenturesSpider


class Fin0004Spider(GGVenturesSpider):
    name = 'fin_0004'
    start_urls = ['https://www.utu.fi/en/university/contact-information']
    country = "Finland"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Turku School of Economics"
    static_logo = "https://www.ercis.org/sites/ercis/files/structure/network/partners/turku.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.utu.fi/en/event-search"

    university_contact_info_xpath = "//div[contains(@class,'region--content')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'There are no upcoming events to display at this time.')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[contains(@rel,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//h2[contains(@class,'aalto-listing-row__title')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.utu.fi/en/news/events']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1/span"))).get_attribute('textContent')
                    try:
                        item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event__body')]").text
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event__body')]").text

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event__time-value')]").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event__time-value')]").text
                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-contact-card')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
