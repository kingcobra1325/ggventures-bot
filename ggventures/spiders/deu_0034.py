from spider_template import GGVenturesSpider


class Deu0034Spider(GGVenturesSpider):
    name = 'deu_0034'
    start_urls = ["https://portal.uni-koeln.de/en/contact"]
    country = 'Germany'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universität zu Köln,Faculty of Management"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Siegel_Uni-Koeln_%28Grau%29.svg/1200px-Siegel_Uni-Koeln_%28Grau%29.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://wiso.uni-koeln.de/en/"

    university_contact_info_xpath = "//div[@id='c39518']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h4/a",next_page_xpath="//span[text()='Weiter']/..",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'eventlist')]//article/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://wiso.uni-koeln.de/"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1[starts-with(@class,'uzk15__standard_h1')]"))).get_attribute('textContent')
                    item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//main[@id='contentstart']").text

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                    try:
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//p[@Class='uzk15__light_wiso']").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//p[@Class='uzk15__light_wiso']").get_attribute('textContent')
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                        # logger.debug(f"XPATH not found {e}: Skipping.....")
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

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
