from spider_template import GGVenturesSpider


class Aus0011Spider(GGVenturesSpider):
    name = 'aus_0011'
    country = 'Australia'
    start_urls = ["https://www.mq.edu.au/about/about-the-university/our-faculties/business/contact-us"]

    # eventbrite_id = 1412983127
    handle_httpstatus_list = [301,302,403,404,410]

    static_name = "Macquarie University,Macquarie Graduate School of Management"
    
    static_logo = "https://logos-download.com/wp-content/uploads/2021/01/Macquarie_Graduate_School_of_Management_Logo.png"

    parse_code_link = "https://www.mq.edu.au/about/about-the-university/events"

    university_contact_info_xpath = "//div[@id='content_container_1210750']/.."
    # contact_info_text = True
    contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            for link in self.events_list(event_links_xpath="//a[@class='h3']"):
                # for link in self.multi_event_pages(event_links_xpath="//a[@class='slide-image']",next_page_xpath="//a[contains(@class,'next_page')]",get_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["https://event.mq.edu.au/"]):

                    self.logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'h1')]"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='page_0']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='page_0']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='page_0']"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[text()='Event contact details']/following-sibling::ul"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
