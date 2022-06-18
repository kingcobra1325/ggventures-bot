from spider_template import GGVenturesSpider


class Aus0003Spider(GGVenturesSpider):
    name = 'aus_0003'
    start_urls = ["https://www.cqu.edu.au/about-us/structure/organisation/university-contacts"]
    country = 'Australia'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Central Queensland University,Faculty of Business and Law"
    
    static_logo = "https://www.cqu.edu.au/__data/assets/git_bridge/0037/67897/dist/mysource_files/cqu-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.cqu.edu.au/events"

    university_contact_info_xpath = "//div[@id='content_container_109968_15678']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='ct-tile__copy']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.cqu.edu.au/events/event-items/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='event-details__descripton']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event-details__info__col']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-details__info__col']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[text()='Contact']/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
