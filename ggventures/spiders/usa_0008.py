from spider_template import GGVenturesSpider


class Usa0008Spider(GGVenturesSpider):
    name = 'usa_0008'
    start_urls = ["https://www.bc.edu/content/bc-web/schools/carroll-school/about/contact.html"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Boston College,Carroll School of Management"
    
    static_logo = "https://www.bentley.edu/themes/custom/bentley/images/logo_2020.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://events.bc.edu/calendar"

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
            for link in self.events_list(event_links_xpath="//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://events.bc.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='summary']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//p[@class='description']","//div[@class='description']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='dateright']"])
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='dateright']"])
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//dt[text()='Contact']/.."],error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
