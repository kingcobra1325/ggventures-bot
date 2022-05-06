from spider_template import GGVenturesSpider


class Esp0009Spider(GGVenturesSpider):
    name = 'esp_0014'
    start_urls = ["https://www.ie.edu/business-school/contact/"]
    country = 'Spain'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "IE - Instituto de Empresa,Business School"
    
    static_logo = "https://static-frm.ie.edu/business-school/wp-content/uploads/sites/41/2019/12/IE-Business-School.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ie.edu/business-school/news-and-events/whats-coming-up/?locality=0"

    university_contact_info_xpath = "//div[@class='content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='bottom_text']/following-sibling::a[1]",next_page_xpath="//li[@class='active']/..",get_next_month=True,page_element="//li",current_page_class="active",next_page_set_xpath="//a[starts-with(@class,'pagination_next')]"):
            # for link in self.events_list(event_links_xpath="//p[@class='bottom_text']/following-sibling::a[1]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://events.ie.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.desc_images(desc_xpath="//div[starts-with(@class,'descripcion-evento')]")

                    item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[@itemprop='startDate']").get_attribute('textContent')
                    item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='TIME']/..").get_attribute('textContent')
                    
                    # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Datum:']/.. | //i[starts-with(@class,'fal')]/../following-sibling::span").get_attribute('textContent')
                    #     item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Tijd:']/..").get_attribute('textContent')
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    try:
                        item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='sidebar-eventos__organize']").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
                    # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
