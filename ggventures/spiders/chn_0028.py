from spider_template import GGVenturesSpider


class Chn0028Spider(GGVenturesSpider):
    name = 'chn_0028'
    start_urls = ["https://www.ruc.edu.cn/useful-contacts-en"]
    country = 'China'
    # eventbrite_id = 6221361805
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Renmin University Of China"
    
    static_logo = "https://www.ruc.edu.cn/wp-content/themes/rucweb/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "http://iss.ruc.edu.cn/events.php"

    university_contact_info_xpath = "//div[@class='nc_body']"
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
            
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[starts-with(@class,'item')]/a",next_page_xpath="//a[@class='next']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            raw_event_times = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//a[contains(@class,'event')]/parent::p/preceding-sibling::p")))
            event_times = [x.text for x in raw_event_times]
            for link in self.events_list(event_links_xpath="//a[contains(@class,'event')]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["ruc.edu.cn/events_info"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    datetime = event_times.pop(0)
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='main_tt2']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='main_content']"],method='attr')
                    item_data['event_date'] = datetime
                    item_data['event_time'] = datetime

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//dd[contains(@class,'sys_events-contact')]"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link


                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
