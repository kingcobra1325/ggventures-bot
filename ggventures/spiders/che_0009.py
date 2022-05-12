from spider_template import GGVenturesSpider


class Che0009Spider(GGVenturesSpider):
    name = 'che_0009'
    start_urls = ["https://www.unil.ch/hec/en/home/contact.html"]
    country = 'Switzerland'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Université de Lausanne - HEC Lausanne"
    
    static_logo = "https://www.unil.ch/modules/unil-core/img/unil-logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.unil.ch/hec/en/home/news.html?actunilParam=events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='col-xs-12']/a",next_page_xpath="//a[@aria-label='Next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://agenda.unil.ch/display/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h2"))).get_attribute('textContent')
                    
                    # item_data['event_desc'] = self.desc_images(desc_xpath="//p[@class='text-justify']/following-sibling::p ")
                    
                    try:
                        item_data['event_desc'] = self.desc_images(desc_xpath="//p[@class='text-justify']/following-sibling::p ")   
                    except self.Exc.NoSuchElementException as e:
                        item_data['event_desc'] = self.desc_images(desc_xpath="(//span[@class='z-html']//div[starts-with(@class,'col-xs-12')])[5]")   
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//p[@class='event_date']").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//p[@class='event_date']").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='well']").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='well']").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='well']").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
                    # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
