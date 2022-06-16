from spider_template import GGVenturesSpider

class Hkg0004Spider(GGVenturesSpider):
    name = 'hkg_0004'
    start_urls = ['https://www.cuhk.edu.hk/english/contact.html']
    country = "Hong Kong"
    # eventbrite_id = 30819498834
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The Chinese University of Hong Kong,Faculty of Business Administration"
    static_logo = "https://www.cuhk.edu.hk/adm/jupas/PED/assets/images/cu-logo-4c-horizontal.gif"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.cuhk.edu.hk/english/university/events.html"

    university_contact_info_xpath = "//div[contains(@id,'main_content')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'There are no upcoming events to display at this time.')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=1,event_links_xpath="//a[@class='title']",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=False,click_month_list_xpath="//a[@class='month']",wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//a[@class='title']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.cpr.cuhk.edu.hk/en/event']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='event-title']/h2"))).text
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='event-text']").text

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='event-text']").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='event-text']").text

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'content')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'content')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....","debug")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'information')]").text
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
