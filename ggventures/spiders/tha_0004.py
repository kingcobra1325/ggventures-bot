from spider_template import GGVenturesSpider


class Tha0004Spider(GGVenturesSpider):
    name = 'tha_0004'
    start_urls = ["https://www.ku.ac.th/en/phone-number"]
    country = 'Thailand'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Kasetsart University,Faculty of Business Administration"
    
    static_logo = "https://www.ku.ac.th/assets/images/header/KU_name_logo_62x62.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ku.ac.th/en/calendar"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//a[text()='List']"))).click()
            self.check_website_changed(upcoming_events_xpath="//div[@aria-labelledby='calendar-all-tab']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='listItemWrap']/a",next_page_xpath="//a[@class='nextPage']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[@class='event_box_title']/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://www.agenda.uzh.ch/record.php"]):
                    
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

            #         item_data = self.item_data_empty.copy()
                    
            #         item_data['event_link'] = link

            #         item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//span[@class='event_title']"))).get_attribute('textContent')
                    
            #         item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='content']")

            #         item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'eventItem')]").get_attribute('textContent')
            #         item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'eventItem')]").get_attribute('textContent')
                    
            #         # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

            #         # try:
            #         #     item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Datum:']/.. | //i[starts-with(@class,'fal')]/../following-sibling::span").get_attribute('textContent')
            #         #     item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Tijd:']/..").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
            #             # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
            #             # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

            #         # try:
            #         #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
            #         # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
