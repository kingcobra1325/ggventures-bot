from spider_template import GGVenturesSpider


class Cze0005Spider(GGVenturesSpider):
    name = "cze_0005"
    start_urls = ["https://www.vse.cz/english/"]
    country = "Czech Republic"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University Of Economics Prague"
    
    static_logo = "https://www.vse.cz/english/wp-content/themes/vse-redesigned/dist/img/logo/logo-full-en-white.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://kalendar.vse.cz/english/"

    university_contact_info_xpath = "//footer[contains(@class,'footer-address')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//button[starts-with(@class,'fusion-load-more-button')]",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2/a",next_page_xpath="//div[contains(@class,'nav-calendar-next')]/a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[@class='fusion-events-wrapper']//h2/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["kalendar.vse.cz/english/event"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//table[contains(@class,'event-detail-basic-info')]/following-sibling::div"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//th[text()='Start:']/.."],method='attr',error_when_none=False,wait_time=5).replace(".\xa0","")
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//table[contains(@class,'event-detail-basic-info')]"],method='attr',error_when_none=False,wait_time=5).replace(".\xa0","")
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//th[text()='Contact person:']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
