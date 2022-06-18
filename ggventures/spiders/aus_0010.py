from spider_template import GGVenturesSpider


class Aus0010Spider(GGVenturesSpider):
    name = 'aus_0010'
    start_urls = ["https://www.latrobe.edu.au/contact"]
    country = 'Australia'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "La Trobe University,School of Business"
    
    static_logo = "https://www.latrobe.edu.au/_media/la-trobe-api/v5/img/logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.latrobe.edu.au/business/news-and-events"

    university_contact_info_xpath = "//div[@class='ds-accordion']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            self.check_website_changed(upcoming_events_xpath="//div[@id='Upcoming-Events']//p[text()='No upcoming events at the moment. Check back soon.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//h3/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://www.curtin.edu.au/events/"]):
                    
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

            #         item_data = self.item_data_empty.copy()
                    
            #         item_data['event_link'] = link

            #         item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[starts-with(@class,'event-title')]"])
            #         item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='row']/div"],enable_desc_image=True)
            #         item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[text()='date']/.."],method='attr',error_when_none=False)
            #         item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[text()='Time']/.."],method='attr',error_when_none=False)
            #         item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[text()='Event contact details']/following-sibling::ul"],method='attr',error_when_none=False,wait_time=5)

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
