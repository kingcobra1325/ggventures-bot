from spider_template import GGVenturesSpider


class Usa0133Spider(GGVenturesSpider):
    name = 'usa_0133'
    start_urls = ["https://www.sandiego.edu/business/about/contact.php"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of San Diego (USD),School of Business Administration"
    
    static_logo = "https://marvel-b1-cdn.bc0a.com/f00000000255490/www.sandiego.edu/business/images/knauss/KSB-Logo-horiz.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.sandiego.edu/events/business/"

    university_contact_info_xpath = "//div[@role='main']"
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//p[@class='title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.sandiego.edu/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@itemprop='name']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//span[@itemprop='description']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@itemprop='startDate']/following-sibling::ul"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@itemprop='startDate']/following-sibling::ul"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h2[text()='Post Contact']/following-sibling::p"],error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
