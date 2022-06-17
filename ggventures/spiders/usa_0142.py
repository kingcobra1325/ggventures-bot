from spider_template import GGVenturesSpider


class Usa0142Spider(GGVenturesSpider):
    name = 'usa_0142'
    start_urls = ["https://foster.uw.edu/contacts/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Washington,Business School"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/University_of_Washington_seal.svg/800px-University_of_Washington_seal.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://foster.uw.edu/news-events/trumba/"

    university_contact_info_xpath = "//div[@class='entry-content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.3.iframe']")))
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="twDescription",next_page_xpath="//span[@class='tribe-events-c-nav__next-label']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//span[@class='twDescription']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://foster.uw.edu/news-events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    self.Mth.WebDriverWait(self.getter, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.3.iframe']")))
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='twEDDescription']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//span[text()='Description']/ancestor::tr[1]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[text()='When']/ancestor::tr[1]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[text()='When']/ancestor::tr[1]"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-block tribe-block__organizer__details')]"],method='attr',error_when_none=False,wait_time=5)
                    if item_data['event_time']:
                        item_data['event_time'] = item_data['event_time'].replace(r"\xa0","")

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
