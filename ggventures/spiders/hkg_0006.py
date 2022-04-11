from spider_template import GGVenturesSpider

class Hkg0006Spider(GGVenturesSpider):
    name = 'hkg_0006'
    start_urls = ['https://www.hkubs.hku.hk/about-us/contact-us/']
    country = "Hong Kong"
    # eventbrite_id = 30819498834
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The Hong Kong Polytechnic University,Faculty of Business"
    static_logo = "https://www.hkubs.hku.hk/wp-content/uploads/2021/01/logo-1.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.hkubs.hku.hk/event/"

    university_contact_info_xpath = "//div[@id='main-content']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'There are no upcoming events to display at this time.')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            for link in self.multi_event_pages(num_of_pages=4,event_links_xpath="//div[contains(@class,'blog-post_title')]/a",next_page_xpath="//a[contains(@class,'next page-numbers')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//p[@class='ev-blk__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.hkubs.hku.hk/event']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2"))).text
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='article-content']").text
                    # try:
                    #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='content']").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='blog-post_datetime']").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='blog-post_datetime']").text

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

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(@class,'ppl-info-line')]").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
