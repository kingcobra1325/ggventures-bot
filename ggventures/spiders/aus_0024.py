from spider_template import GGVenturesSpider


class Aus0024Spider(GGVenturesSpider):
    name = 'aus_0024'
    start_urls = ["https://www.canberra.edu.au/about-uc/faculties/busgovlaw/contact-us"]
    country = "Australia"
    # eventbrite_id = 12790629019

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Canberra,School of Business"
    
    static_logo = "https://www.canberra.edu.au/_designs/ucweb/common/images/logo/uc_logo_inline.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.canberra.edu.au/events/"

    university_contact_info_xpath = "//tbody"
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//a[@class='nostyle']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.canberra.edu.au/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='pt-2']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'pt-3')]"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'data-background')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'data-background')]"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h4[text()=' Enquiry']/../.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
