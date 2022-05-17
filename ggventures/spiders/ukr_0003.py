from spider_template import GGVenturesSpider


class Ukr0003Spider(GGVenturesSpider):
    name = 'ukr_0003'
    start_urls = ["https://kneu.edu.ua/en/pin_information_eapk/"]
    country = 'Ukraine'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "KNEU - Kiev National Economic University"
    
    static_logo = "https://kneu.edu.ua/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://kneu.edu.ua/en/events/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='listItemWrap']/a",next_page_xpath="//a[@class='nextPage']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//li[@class='clearfix']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://kneu.edu.ua/en/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='article']//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='aside']"],method='attr',enable_desc_image=True)
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["(//div[starts-with(@class,'vc_column-inner')])[2]"],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["(//div[starts-with(@class,'vc_column-inner')])[2]"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
