from spider_template import GGVenturesSpider


class Tha0001Spider(GGVenturesSpider):
    name = 'tha_0001'
    start_urls = ["https://www.som.ait.ac.th/contact-us"]
    country = 'Thailand'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Asian Institute of Technology (AIT),School of Management"
    
    static_logo = "https://static.wixstatic.com/media/9f6cd0_d5d3fe3621bb4e3dbc9923838ec2267e~mv2.png/v1/crop/x_0,y_2,w_268,h_83/fill/w_178,h_55,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/SOM_Logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ait.ac.th/events/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            self.check_website_changed(upcoming_events_xpath="//h1[text()='Missing Calendar']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='listItemWrap']/a",next_page_xpath="//a[@class='nextPage']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[@class='event_box_title']/a"):
            #     self.getter.get(link) 
            #     if self.unique_event_checker(url_substring=["https://www.agenda.uzh.ch/record.php"]):
                    
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

            #         item_data = self.item_data_empty.copy()
                    
            #         item_data['event_link'] = link

            #         item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//span[@class='event_title']"))).get_attribute('textContent')
                    
            #         item_data['event_desc'] = self.desc_images(desc_xpath="//div[@class='content']")

            #         item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'eventItem')]").get_attribute('textContent')
            #         item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[starts-with(@class,'eventItem')]").get_attribute('textContent')
                    
            #         # item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')

            #         # try:
            #         #     item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Datum:']/.. | //i[starts-with(@class,'fal')]/../following-sibling::span").get_attribute('textContent')
            #         #     item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[text()='Tijd:']/..").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
            #             # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')
            #             # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'inner-box information')]").get_attribute('textContent')

            #         # try:
            #         #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//table[@class='event-table']").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....")
                    
            #         # self.get_emails_from_source(driver_name='getter',attribute_name='href',tag_list=['a'])

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
