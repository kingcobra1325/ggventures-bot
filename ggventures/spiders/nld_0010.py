from spider_template import GGVenturesSpider


class Nld0010Spider(GGVenturesSpider):
    name = 'nld_0010'
    start_urls = ["https://tsm.nl/contact/"]
    country = 'Netherlands'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "TSM Business School"
    
    static_logo = "https://tsm.nl/wp-content/uploads/2021/02/cropped-Artboard.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://tsm.nl/agenda/"

    university_contact_info_xpath = "//h3[text()='Contactgegevens']/.."
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
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[starts-with(@class,'tribe-events-calendar-list__event-title')]",next_page_xpath="//span[@class='pagi-cta']/a[2]",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//h2/following-sibling::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://tsm.nl/proefcollege/","https://tsm.nl/opleiding/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1[@class='block__title']"))).get_attribute('textContent')
                    
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//h1[@class='block__title']/.."],method='attr')

                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//section[contains(@class,'section')]","//span[text()='Datum:']/..","//i[starts-with(@class,'fal')]/../following-sibling::span"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//section[contains(@class,'section')]","//span[text()='Tijd:']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
