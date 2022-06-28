from spider_template import GGVenturesSpider


class Pol0010Spider(GGVenturesSpider):
    name = 'pol_0010'
    start_urls = ["https://ue.poznan.pl/pl/uniwersytet,c13/administracja-i-jednostki-uep,c9844/centrum-edukacji-menedzerskiej,c1383/kontakt,a8119.html"]
    country = 'Poland'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Wielkopolska Business School"
    
    static_logo = "https://ue.poznan.pl/themes/img/logo_pl.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ue.poznan.pl/pl/aktualnosci,c16/kalendarz-wydarzen,c151/"

    university_contact_info_xpath = "//div[@class='g_6of6 _cf']"
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
            
            raw_event_times = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//h3[contains(text(),'Nadchodzące')]/following-sibling::ul//a/span")))
            event_times = [x.text for x in raw_event_times]
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[starts-with(@class,'tribe-events-calendar-list__event-title')]",next_page_xpath="//span[@class='pagi-cta']/a[2]",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//h3[contains(text(),'Nadchodzące')]/following-sibling::ul//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://ue.poznan.pl/pl/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1[@class='t_size-50']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//section[@class='m_big']")

                    event_times_popped = event_times.pop(0)
                    item_data['event_date'] = event_times_popped
                    item_data['event_time'] = event_times_popped
                    
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
