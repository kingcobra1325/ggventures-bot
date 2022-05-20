from spider_template import GGVenturesSpider


class Rus0017Spider(GGVenturesSpider):
    name = 'rus_0017'
    start_urls = ["https://guu.ru/%D0%BE%D0%B1-%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D0%B5/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F/"]
    country = 'Russia'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "State University of Management,Higher School of Business"
    
    static_logo = "https://guu.ru/assets/img/logo_en.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://unecon.ru/info/anonsy"

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
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'event-calendar__day-wrap')]//a",next_page_xpath="//span[starts-with(@class,'icon-arrow-calendar')][2]",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@id='content']/div/h2/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://unecon.ru/info/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2[@class='title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='node-content']"],method='attr',enable_desc_image=True)
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event-info']"],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-info']"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
