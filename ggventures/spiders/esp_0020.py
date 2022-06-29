from spider_template import GGVenturesSpider


class Esp0020Spider(GGVenturesSpider):
    name = 'esp_0020'
    start_urls = ["https://www.deusto.es/en/home/contact"]
    country = 'Spain'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universidad Comercial de Deusto"
    
    static_logo = "https://www.deusto.es/estaticos/ud/img/logoDeustoMenu-en.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://agenda.deusto.es/en/?view=list&campus=a%3A4%3A%7Bi%3A0%3Bs%3A1%3A%221%22%3Bi%3A1%3Bs%3A1%3A%222%22%3Bi%3A2%3Bs%3A1%3A%223%22%3Bi%3A3%3Bs%3A1%3A%224%22%3B%7D&facultades=a%3A1%3A%7Bi%3A0%3Bs%3A1%3A%222%22%3B%7D&tematicas=a%3A3%3A%7Bi%3A0%3Bs%3A2%3A%2214%22%3Bi%3A1%3Bs%3A2%3A%2213%22%3Bi%3A2%3Bs%3A2%3A%2216%22%3B%7D"

    university_contact_info_xpath = "//section"
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
            for link in self.events_list(event_links_xpath="//div[@class='evento_dia_texto']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://agenda.deusto.es/en/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1[@class='entry-title']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[@id='event_post_description']")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='evento_dia_datos_fecha']").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='evento_dia_datos_hora']").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='evento_dia_datos_fecha']").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='evento_dia_datos_hora']").get_attribute('textContent')
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
