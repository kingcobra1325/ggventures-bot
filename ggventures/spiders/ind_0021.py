from spider_template import GGVenturesSpider


class Ind0021Spider(GGVenturesSpider):
    name = 'ind_0021'
    start_urls = ["https://krea.edu.in/ifmrgsb/contact/"]
    country = 'India'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Institute for Financial Management & Research (IFMR)"
    
    static_logo = "https://krea.edu.in/ifmrgsb/wp-content/uploads/2020/08/IFMR-Normal.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://krea.edu.in/ifmrgsb/events/#events"

    university_contact_info_xpath = "//div[@class='elementor-inner']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//button[@type='button']"))).click()
            self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//a[text()='Next Year']"))).click() 
    
            self.check_website_changed(upcoming_events_xpath="//div[contains(text(),'There are no events ')]",empty_text=False)
            
            # self.ClickMore(click_xpath="//strong[text()='Load more listings']",run_script=True)
            
            # # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[contains(@class,'tabpanel--active')]//div[contains(@class,'slick-active')]//h3/a",next_page_xpath="//a[contains(@class,'nextBtn')]",get_next_month=False,click_next_month=True,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//div[starts-with(@class,'event_listing')]"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://krea.edu.in/ifmrgsb/event/"]):
                    
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

            #         item_data = self.item_data_empty.copy()
                    
            #         item_data['event_link'] = link

            #         item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='section']//h3"))).get_attribute('textContent')
                    
            #         item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='acc-text']")

            #         # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
            #         # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

            #         try:
            #             item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[@class='span01']").get_attribute('textContent')
            #             item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[@class='span03']").get_attribute('textContent')
            #         except self.Exc.NoSuchElementException as e:
            #             self.Func.print_log(f"XPATH not found {e}: Skipping.....")
            #             # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
            #             # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

            #         # try:
            #         #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(text(),'Kontakt')]/following-sibling::div").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
