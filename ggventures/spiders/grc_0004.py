from spider_template import GGVenturesSpider


class Grc0004Spider(GGVenturesSpider):
    name = 'grc_0004'
    start_urls = ['https://york.citycollege.eu/m/articles.php?cid=126&t=Contact-us-BAED']
    country = "Greece"
    # eventbrite_id = 30819498834
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "City Liberal Studies (City College),Business Administration & Economics"
    static_logo = "https://york.citycollege.eu/m/templates_mobile/mobile_city_2016/images/logo_city_mobile.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://york.citycollege.eu/m/news.php?cid=12"

    university_contact_info_xpath = "//div[contains(@class,'article_content')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'There are no upcoming events to display at this time.')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[contains(@class,'tribe-events-loop')]//h3/a",next_page_xpath="//a[@rel='next']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//ul[@data-role='listview']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['york.citycollege.eu/m/article.php']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1[@class='article_title']"))).text
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//h1[@class='article_title']/following-sibling::div").text

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//h1[@class='article_title']/following-sibling::div").text
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//h1[@class='article_title']/following-sibling::div").text
                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event-email-phone')]").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
