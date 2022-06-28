from spider_template import GGVenturesSpider


class Bel0006Spider(GGVenturesSpider):
    name = "bel_0006"
    start_urls = ["https://www.vlerick.com/en/contact-us/"]
    country = "Belgium"
    # eventbrite_id = 12790629019

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Vlerick Leuven Gent Management School"
    
    static_logo = "https://www.vlerick.com/img/logo--portrait.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.vlerick.com/en/events/"

    university_contact_info_xpath = "//div[contains(@data-kontent-add-button-insert-position,'end')]//div[contains(@class,'justify-content-center row')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//span[contains(text(),'More info')]/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["vlerick.com/en/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1/parent::div"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@id,'vlerick:body')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'c-hero__programme-detail-content')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'c-hero__programme-detail-content')]"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'c-contact-card')]"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
