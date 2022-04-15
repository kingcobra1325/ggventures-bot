from spider_template import GGVenturesSpider


class Ita0017Spider(GGVenturesSpider):
    name = 'ita_0017'
    start_urls = ["https://en.unisi.it/"]
    country = 'Italy'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Università degli Studi di Siena,Facoltà di Economia \"Richard M. Goodwin\""
    
    static_logo = "https://www.unisi.it/sites/all/themes/unisi/logo_unisi.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://businessschool.luiss.it/en/news-events/calendar/"

    university_contact_info_xpath = "//strong[text()='Università degli Studi di Siena']/.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[starts-with(@class,'tribe-events-calendar-list__event-title')]",next_page_xpath="//span[@class='pagi-cta']/a[2]",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//h5[@class='header-image']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://businessschool.luiss.it/en/evento/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='page-title']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='main-text']")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[text()='Date']/../..").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//strong[text()='Date']/../..").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(text(),'Kontakt')]/following-sibling::div").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
                    # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
