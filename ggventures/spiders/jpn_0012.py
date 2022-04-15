from spider_template import GGVenturesSpider


class Jpn0012Spider(GGVenturesSpider):
    name = 'jpn_0012'
    start_urls = ["https://www.meiji.ac.jp/cip/english/contact.html"]
    country = 'Japan'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Meiji University"
    
    static_logo = "https://www.meiji.ac.jp/cip/english/common/ssi/t4q24j0000000t7k-img/logo_univ.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.meiji.ac.jp/cip/english/news/2022/index.html"

    university_contact_info_xpath = "//div[@class='contents ']"
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
            for link in self.events_list(event_links_xpath="//li[starts-with(@class,'js-slide')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.meiji.ac.jp/cip/english/news/","https://english-meiji.net/articles/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2[@class='title'] | //main//h1/span"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[starts-with(@class,'DetailTxt ')] | //div[@class='article-body ']")

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
