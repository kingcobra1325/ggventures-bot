from spider_template import GGVenturesSpider


class Usa0057Spider(GGVenturesSpider):
    name = 'usa_0057'
    start_urls = ["https://krannert.purdue.edu/fast-tracks/contact.php"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Purdue University,Krannert School of Management"
    
    static_logo = "https://krannert.purdue.edu/includes/img/KRN-WG-H-RGB.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://krannert.purdue.edu/alumni/event/home.php?"

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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//p/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://krannert.purdue.edu/alumni/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//article/h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//article"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//article"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//article"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[text()='Contact Info']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
