from spider_template import GGVenturesSpider


class Usa0094Spider(GGVenturesSpider):
    name = 'usa_0094'
    start_urls = ["https://utulsa.edu/news-media/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of Tulsa,College of Business Administration"
    
    static_logo = "https://mbaonline.utulsa.edu/images/logo_hu89d1e5a616bdaec5675d8d39719b6f07_457375_960x0_resize_q90_lanczos_2.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://calendar.utulsa.edu/events/category/college-of-business/"

    university_contact_info_xpath = "//div[@id='primary']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.check_website_changed(upcoming_events_xpath="//li[contains(text(),'No matching events')]",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='eventHeader']/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://events.uiowa.edu/"]):
                    
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

            #         item_data = self.item_data_empty.copy()
                    
            #         item_data['event_link'] = link

            #         item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
            #         item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='description']"],enable_desc_image=True,error_when_none=False)
            #         item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='date']"],method='attr',error_when_none=False)
            #         item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='time']"],method='attr',error_when_none=False)
            #         item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//a[@id='contactName']/ancestor::div[1]"],method='attr',error_when_none=False)

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
