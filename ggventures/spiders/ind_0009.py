from spider_template import GGVenturesSpider


class Ind0009Spider(GGVenturesSpider):
    name = 'ind_0009'
    start_urls = ["https://gim.ac.in/contact-us"]
    country = 'India'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Goa Institute of Management (GIM)"
    
    static_logo = "https://gim.ac.in/modules/custom/custom_menu/img/gim-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://gim.ac.in/institute/events"

    university_contact_info_xpath = "//h4[text()='Hotline']/../../../../../../../.."
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
                
                # if self.unique_event_checker(url_substring=["https://christuniversity.in/events"]):
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//h2[text()='Upcoming Events']/following::div[starts-with(@class,'slick-slide')]"):
                self.Func.print_log(f"Currently scraping --> {link}","info")

                item_data = self.item_data_empty.copy()
                
                # item_data['event_link'] = link

                item_data['event_name'] = self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//strong"))).get_attribute('textContent')
                
                try:
                    item_data['event_desc'] = self.driver.find_element(self.Mth.By.XPATH,"//div[@class='evnt-contnt']/p").get_attribute('textContent')
                except self.Exc.NoSuchElementException as e:
                    self.Func.print_log(f'XPATH not found: {e}: Skipping.....')

                # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
                # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

                try:
                    item_data['event_date'] = self.driver.find_element(self.Mth.By.XPATH,"//div[@class='text']/p").get_attribute('textContent')
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='elementObjectEventMultiTime']").get_attribute('textContent')
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
