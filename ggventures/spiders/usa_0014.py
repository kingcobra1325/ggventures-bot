from spider_template import GGVenturesSpider


class Usa0014Spider(GGVenturesSpider):
    name = 'usa_0014'
    start_urls = ["https://www.cmu.edu/tepper/contact-us.html"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Carnegie Mellon University,Carnegie Bosch Institute - Tepper School of Business"
    
    static_logo = "https://www.cmu.edu/tepper/images/assets/images/block-t-300x300-min.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.cmu.edu/tepper/news/events/index.html"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='em-card_image']/a",next_page_xpath="(//div[@class='em-search-pagination']//i)[2]/..",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='calendar']")))
            self.events_click_reveal(click_area_xpath="//div[@class='agendaItem__summary']")
            
            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'d-text ')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://cmucommunity.force.com/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='evt_h1_outer_box']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='evt_box_body']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='evt_box_body']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='evt_box_body']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[contains(text(),'Contact')]/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
