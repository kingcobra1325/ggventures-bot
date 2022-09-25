from spider_template import GGVenturesSpider


class Aus0012Spider(GGVenturesSpider):
    name = 'aus_0012'
    country = 'Australia'
    start_urls = ["https://mbs.edu/about-us/contact-us"]

    eventbrite_id = 27447427417
    handle_httpstatus_list = [301,302,403,404,410]

    static_name = "Melbourne Business School,The University of Melbourne"
    
    static_logo = "https://mbs.edu/assets/images/mbs-logo.png"

    parse_code_link = "https://mbs.edu/events?categories=School-Events"

    university_contact_info_xpath = "//div[@class='page-content']"
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            for link in self.events_list(event_links_xpath="//div[@class='event-text-wrapper']/h2/a"):
                # for link in self.multi_event_pages(event_links_xpath="//a[@class='slide-image']",next_page_xpath="//a[contains(@class,'next_page')]",get_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://mbs.edu/events/"]):

                    self.logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='display-large']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//section[@class='s-event-detail']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='page-details']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='page-details']"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[text()='Event contact details']/following-sibling::ul"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
