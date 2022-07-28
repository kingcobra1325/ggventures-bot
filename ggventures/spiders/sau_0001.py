from spider_template import GGVenturesSpider


class Sau0001Spider(GGVenturesSpider):
    name = 'sau_0001'
    start_urls = ['https://www.arabou.edu.sa/directory/Pages/find-by-name.aspx']
    country = "Saudi Arabia"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Arab Open University (AOU)"
    static_logo = "https://www.arabou.edu.sa/assets/common/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.arabou.edu.sa/media/pages/events.aspx"

    university_contact_info_xpath = "//div[@class='aou-footer']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//main",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'moreListing')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=5,event_links_xpath="//h5/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@class='event-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['arabou.edu.sa']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'events-title')]"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='events-body']"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'events-date')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'events-date')]"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='evento-cont']"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
