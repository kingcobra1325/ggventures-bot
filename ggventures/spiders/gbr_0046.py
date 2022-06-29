from spider_template import GGVenturesSpider

class Gbr0046Spider(GGVenturesSpider):
    name = 'gbr_0046'
    country = 'United Kingdom'
    start_urls = ["https://www.surrey.ac.uk/business-school"]
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Surrey,School of Management"
    
    static_logo = "https://www.surrey.ac.uk/themes/custom/surrey/logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.surrey.ac.uk/business-school/events"

    university_contact_info_xpath = "//span[contains(text(),'Phone')]/../.."
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
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[contains(@class,'teal')]",next_page_xpath="//a[@title='Page ›']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//article/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["surrey.ac.uk/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1/span"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='body-content']"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//h5[starts-with(@class,'text-uppercase')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//h5[@class='text-pale-gray']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Contact')]/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
