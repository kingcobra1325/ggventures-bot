from spider_template import GGVenturesSpider


class Ind0025Spider(GGVenturesSpider):
    name = 'ind_0025'
    start_urls = ["https://www.irma.ac.in/contact-us"]
    country = 'India'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Institute of Rural Managament - Anand"
    
    static_logo = "https://www.irma.ac.in/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.imt.edu/"

    university_contact_info_xpath = "//section[2]"
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
            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'et_pb_column et_pb_column_1_3 et_pb_column_3 ')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://bfsi.economictimes.indiatimes.com/news/","https://www.educationtimes.com/article/","https://www.businessbecause.com/news/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1[@class='text-no-capital'] | //div[@class='arclpage']/h1 | //div[contains(@class,'content-box')]//h1"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//section[@id='main-content'] | //div[@class='imgarttx'] | //div[contains(@class,'content-box')]//div[@class='Normal']")

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='calendar']/.. |  //div[@class='arclpage']/p | //li[@class='date']").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='calendar']/.. |  //div[@class='arclpage']/p | //li[@class='date']").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
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
