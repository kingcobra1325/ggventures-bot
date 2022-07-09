from spider_template import GGVenturesSpider


class Ind0007Spider(GGVenturesSpider):
    name = 'ind_0007'
    start_urls = ["https://christuniversity.in/"]
    country = 'India'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Christ College - Bangalore"
    
    static_logo = "https://christuniversity.in/images/logo.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://christuniversity.in/events"

    university_contact_info_xpath = "//div[@class='footr-itm-d']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h4/a",next_page_xpath="//span[text()='Weiter']/..",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//div[@id='tab4default']//li/a"):
                link.click()
                self.Func.sleep(1)
                # if self.unique_event_checker(url_substring=["https://christuniversity.in/events"]):

                self.Func.print_log(f"Currently scraping --> {self.driver.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//a[contains(text(),'View More')]"))).get_attribute('href')

                item_data['event_name'] = self.driver.find_element(self.Mth.By.XPATH,"//div[@class='evnt-contnt']/h4").text
                
                try:
                    item_data['event_desc'] = "".join([x.text for x in self.driver.find_elements(self.Mth.By.XPATH,"//div[@class='evnt-contnt']/p")])
                except self.Exc.NoSuchElementException as e:
                    self.Func.print_log(f'XPATH not found: {e}: Skipping.....')

                # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                try:
                    item_data['event_date'] = self.driver.find_element(self.Mth.By.XPATH,"//div[@class='evnt-contnt']").get_attribute('textContent')
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='evnt-contnt']").get_attribute('textContent')
                except self.Exc.NoSuchElementException as e:
                    self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    # logger.debug(f"XPATH not found {e}: Skipping.....")
                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                # try:
                #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(text(),'Kontakt')]/following-sibling::div").get_attribute('textContent')
                # except self.Exc.NoSuchElementException as e:
                #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                # item_data['startups_link'] = ''
                # item_data['startups_name'] = ''

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
