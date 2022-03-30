from spider_template import GGVenturesSpider


class Egy0002Spider(GGVenturesSpider):
    name = 'egy_0002'
    start_urls = ['https://www.aucegypt.edu/inquiry']
    country = "Egypt"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "American University in Cairo"
    static_logo = "https://www.aucegypt.edu/sites/default/files/2021-02/WWW.AUC_.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://happening.aucegypt.edu/events/upcoming"

    university_contact_info_xpath = "//h3[contains(text(),'CONTACT INFO')]/parent::div"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[contains(@class,'event-title')]/a",next_page_xpath="//section[contains(@class,'cbs-event-current-pane')]//li[contains(@class,'pager-next')]/a",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'view-id-events')]//div[contains(@class,'event-widget-img-wrapper')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['auc-connect.aucegypt.edu/PUBLICEV']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).text
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@id,'event_details')]").text

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'col-md-4_5')]").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'col-md-4_5')]").text

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'c-contact-card')]").text
                    # except NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
