from spider_template import GGVenturesSpider

class Aus0002Spider(GGVenturesSpider):

    name = 'aus_0002'
    country = 'Australia'
    start_urls = ["https://bond.edu.au/intl/about-bond/academia/bond-business-school"]
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'Bond University,School of Business'
    static_logo = 'https://static.bond.edu.au/sites/all/themes/bond_base/logo.svg'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://bond.edu.au/intl/events'

    TRANSLATE = False

    university_contact_info_xpath = "//h2[text()='Contact us']/.."
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//h4[@class='timeline-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://bond.edu.au/intl/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='container']/article"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Date') or contains(text(),'When')]/.."],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Date') or contains(text(),'When')]/.."],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h3[text()='Contact']/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
