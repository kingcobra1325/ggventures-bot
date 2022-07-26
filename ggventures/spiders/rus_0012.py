from spider_template import GGVenturesSpider


class Rus0012Spider(GGVenturesSpider):
    name = 'rus_0012'
    start_urls = ["https://mgubs.ru/main/contacts/"]
    country = 'Russia'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Moscow State University,Graduate School of Business Administration"
    
    static_logo = "https://mgubs.ru/wp-content/themes/webdmitriev/assets/img/header/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://mgubs.ru/main/all-events/"

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
            for link in self.events_list(event_links_xpath="//section//div[@class='events-items']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://mgubs.ru/allevents/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'main-wrapper__right')]"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='events-date']"],method='attr').replace("\n","")
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='events-date']"],method='attr').replace("\n","")

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
