from spider_template import GGVenturesSpider


class Usa0006Spider(GGVenturesSpider):
    name = 'usa_0006'
    start_urls = ["https://www.baylor.edu/business/index.php?id=87041"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Baylor University - Hankamer School of Business"
    
    static_logo = "https://www.baylor.edu/business/images_3/newLogoWeb.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.baylor.edu/business/news/index.php?id=86163"

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
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='em-card_image']/a",next_page_xpath="(//div[@class='em-search-pagination']//i)[2]/..",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//a[starts-with(@class,'tribe-event-url')]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://zicklin.baruch.cuny.edu/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='tribe-events-single-event-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-single-event-description')]"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'tribe-events-schedule')]"],method='attr')
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h2[text()='Organizer']/.."],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
