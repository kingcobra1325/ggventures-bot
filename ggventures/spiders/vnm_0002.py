from spider_template import GGVenturesSpider


class Vnm0002Spider(GGVenturesSpider):
    name = 'vnm_0002'
    start_urls = ["https://ueh.edu.vn/en/about-us/overview"]
    country = 'Vietnam'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Economics, Ho Chi Minh City (UEH)"
    
    static_logo = "https://ueh.edu.vn/portal-en/img/logo-primary.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ueh.edu.vn/en/events/"

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
            
            # self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'event-calendar__day-wrap')]//a",next_page_xpath="//span[starts-with(@class,'icon-arrow-calendar')][2]",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://ueh.edu.vn/en/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2",])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'col-lg-12')]"],method='attr',enable_desc_image=True)
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='date']",],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-info']"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

            self.driver.get("https://dsa.ueh.edu.vn/en/upcoming-events/")

            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'vc_gitem-zone')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://dsa.ueh.edu.vn/en/news/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='bs-desc']"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//li[@class='bs-date']"],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//blockquote"],method='attr')
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='bs-desc']"],method='attr')


                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
