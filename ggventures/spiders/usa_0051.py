from spider_template import GGVenturesSpider

class Usa0051Spider(GGVenturesSpider):
    name = 'usa_0051'
    country = 'US'
    start_urls = ["https://www.stern.nyu.edu/experience-stern/contact-us"]
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "MIT - Massachusetts Institute of Technology,Sloan School of Management"
    
    static_logo = "https://www.stern.nyu.edu/sites/all/themes/stern/images/logo.nyu-stern.450.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.stern.nyu.edu/experience-stern/news-events/events"

    university_contact_info_xpath = "//div[contains(@class,'paragraphs-item-main-content-component')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='card']/a",next_page_xpath="//a[text()='next ›']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'view-display-id-upcoming_events')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["stern.nyu.edu"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='article']/h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='article-col-main']"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='article-col-main']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='article-col-main']"],method='attr')
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[contains(text(),'Event Cont')]"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)