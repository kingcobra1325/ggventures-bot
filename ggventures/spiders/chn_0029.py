from spider_template import GGVenturesSpider


class Chn0029Spider(GGVenturesSpider):
    name = 'chn_0029'
    start_urls = ["https://english.snnu.edu.cn/Contact_Us1/General_Contact_Information.htm"]
    country = 'China'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Shaanxi Normal University"
    
    static_logo = "https://english.snnu.edu.cn/dfiles/18160/images/logo.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://english.snnu.edu.cn/Events.htm"

    university_contact_info_xpath = "//div[@id='vsb_content']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//article[starts-with(@class,'col-md-12')]/h2/a",next_page_xpath="//tr[@class='calendar-box-header']/th[3]/a",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//li[@class='item1']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://english.snnu.edu.cn/info/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='v_news_content']")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[contains(text(),'Lecture time' )] | //span[contains(text(),'Lecture time')]/../.. | //p[contains(text(),'Date:')] |  //strong[contains(text(),'Time' )]/..").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[contains(text(),'Lecture time' )] | //span[contains(text(),'Lecture time')]/../.. | //p[contains(text(),'Time:')] |  //strong[contains(text(),'Time' )]/..").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[contains(text(),'Lecture time' )] | //span[contains(text(),'Lecture time')]/../.. | //p[contains(text(),'Date:')] |  //strong[contains(text(),'Time' )]/..").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[contains(text(),'Lecture time' )] | //span[contains(text(),'Lecture time')]/../.. | //p[contains(text(),'Time:')] |  //strong[contains(text(),'Time' )]/..").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
                    # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
