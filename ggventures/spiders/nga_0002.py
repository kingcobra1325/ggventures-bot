from spider_template import GGVenturesSpider


class Nga0002Spider(GGVenturesSpider):
    name = 'nga_0002'
    start_urls = ['https://www.lbs.edu.ng/dba/contact-us/']
    country = "Nigeria"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Pan-Atlantic University,Lagos Business School (LBS)"
    static_logo = "http://pau.edu.ng/wp-content/uploads/2021/04/PAU-Logo-GIF3.gif"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.lbs.edu.ng/news/events/"

    university_contact_info_xpath = "//div[@class='contact-items']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            self.check_website_changed(upcoming_events_xpath="//div[@id='events-items']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//h3/a",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False):
            # for link in self.events_list(event_links_xpath="//div[@id='itemListLinks']//a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=['oauife.edu.ng/news-events/item']):
            #
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")
            #
            #         item_data = self.item_data_empty.copy()
            #
            #         item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).text
            #         item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='itemFullText']").text
            #         # try:
            #         #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event-desc')]").text
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
            #
            #         item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='itemFullText']").text
            #         item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='itemFullText']").text
            #
            #         # item_data['event_date'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",'content')
            #         # item_data['event_time'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",'content')
            #
            #         # try:
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....","debug")
            #         #     # logger.debug(f"XPATH not found {e}: Skipping.....")
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #
            #         # try:
            #         #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(text(),'Contact')]/parent::li").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''
            #         item_data['event_link'] = link
            #
            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
