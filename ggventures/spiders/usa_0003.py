from spider_template import GGVenturesSpider


class Usa0003Spider(GGVenturesSpider):
    name = 'usa_0003'
    start_urls = ["https://www.lib.auburn.edu/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Auburn University"
    
    static_logo = "https://www.auburn.edu/template/2022/_assets/images/logos/auburn/formal_horiz/onecolor_white/auburn_formal_h_onecolor_white_web.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://calendar.auburn.edu/calendar"

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
            
            # self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='em-card_image']/a",next_page_xpath="(//div[@class='em-search-pagination']//i)[2]/..",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//a[@class='clearfix']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://calendar.auburn.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='em-header-card_title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='em-content_about']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='em-date']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='em-date']"],method='attr')
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='em-date']"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
