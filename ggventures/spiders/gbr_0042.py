from spider_template import GGVenturesSpider

class Gbr0042Spider(GGVenturesSpider):
    name = 'gbr_0042'
    country = 'United Kingdom'
    start_urls = ["https://www.plymouth.ac.uk/"]
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Plymouth,The Plymouth Business School"
    
    static_logo = "https://d39ner1f41xyl1.cloudfront.net/assets/uopqueenlogomono-156ce0828e4a0d49073bd3135ef7a3f2df130d1ac3612a29a5f0c8d5faf98557.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.plymouth.ac.uk/whats-on/events?tags%5B%5D=events"

    university_contact_info_xpath = "//section[@itemprop='publisher']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='There are no forthcoming events currently listed. Please see the archive for past events.']")
            
            # self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[contains(@class,'teal')]",next_page_xpath="//a[@title='Page ›']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//a[@class='page-item-image-link']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["plymouth.ac.uk"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='hero-heading']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//article[starts-with(@class,'res-article-body')]"],method='attr')
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//time[@itemprop='startDate']"],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//h5[@class='text-pale-gray']"],method='attr',error_when_none=False)
                    
                    item_data['event_date'] = self.get_datetime_attributes("//time[@itemprop='startDate']",'datetime')
                    item_data['event_time'] = self.get_datetime_attributes("//time[@itemprop='startDate']",'datetime')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Contact')]/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)