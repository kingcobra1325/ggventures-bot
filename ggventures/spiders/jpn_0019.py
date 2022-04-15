from spider_template import GGVenturesSpider


class Jpn0019Spider(GGVenturesSpider):
    name = 'jpn_0019'
    start_urls = ["https://www.mbaib.gsbs.tsukuba.ac.jp/contact-us/"]
    country = 'Japan'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Tsukuba,Graduate School of Business Sciences"
    
    static_logo = "https://www.mbaib.gsbs.tsukuba.ac.jp/wp-content/uploads/common/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.mbaib.gsbs.tsukuba.ac.jp/eventlist/"

    university_contact_info_xpath = "//div[@id='main_cont']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True


    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//li[text()='There were no results found.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[starts-with(@class,'tribe-events-calendar-list__event-title')]",next_page_xpath="//span[@class='pagi-cta']/a[2]",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//dd/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.mbaib.gsbs.tsukuba.ac.jp/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@id='page_ttl']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[@id='main_cont']")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//h2").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[@class='field-content']").get_attribute('textContent')
                    #     item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[@class='field-content']").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='article-coordination-info']").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
                    # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
