from spider_template import GGVenturesSpider


class Che0007Spider(GGVenturesSpider):
    name = 'che_0007'
    start_urls = ["https://www.unisg.ch/en/universitaet/besucher/anfahrtundcampusplan/kontaktseite"]
    country = 'Switzerland'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universität St. Gallen"
    
    static_logo = "https://www.unisg.ch/-/media/93125423859d46928371a633b15cfcb1.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.unisg.ch/en/wissen/veranstaltungen"

    university_contact_info_xpath = "//main"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//a[@data-range='this-year']"))).click()
            
            self.Func.sleep(5)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='o_card__head']/a",next_page_xpath="//a[text()='Sig >']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//div[@class='g-metro-item-inner']"):
                # self.getter.get(link)
                # if self.unique_event_checker(url_substring=["https://www.ust.edu.ph/"]):
                    
                self.Func.print_log(f"Currently scraping --> {self.driver.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = response.url

                item_data['event_name'] = self.Mth.WebDriverWait(link,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,".//h3"))).get_attribute('textContent')
                
                # item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='entry-content']")

                item_data['event_date'] = link.find_element(self.Mth.By.XPATH,".//div[@class='e-date-block']").get_attribute('textContent')
                item_data['event_time'] = link.find_element(self.Mth.By.XPATH,".//h4").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Datum:']/.. | //i[starts-with(@class,'fal')]/../following-sibling::span").get_attribute('textContent')
                    #     item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Tijd:']/..").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
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
