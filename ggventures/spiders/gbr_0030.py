from spider_template import GGVenturesSpider

class Gbr0030Spider(GGVenturesSpider):
    name = 'gbr_0030'
    country = 'United Kingdom'
    start_urls = ["https://www.bath.ac.uk/schools/school-of-management/"]
    eventbrite_id = 47699605203
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "University of Bath,School of Management"
    static_logo = "https://www.bath.ac.uk/lens/109/assets/university-of-bath/images/logo/uob-logo-standard.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.bath.ac.uk/events/?f.Department+or+group%7CX=School+of+Management"

    university_contact_info_xpath = "//li[@class='telephone']/../.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # height = self.driver.execute_script("return document.body.scrollHeight")
            # WebScroller(self.driver,height)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//div[contains(@class,'cal_load-button')]/button",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[text()='>>']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//li[@Class='search-result-item']//a"):
                self.logger.debug(f"THIS IS THE LINK: |{link}|")
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['https://mba.bath.ac.uk/','https://www.bath.ac.uk/events']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='section-heading']","//h1[@id='main-content']"],method='attr',error_when_none=False)
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='single-item']","//article[@class='single-item']"],method='attr',error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//li[@aria-label='Time of event']","//strong"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//li[@aria-label='Time of event']","//strong"],method='attr',error_when_none=False)

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[contains(@class,'contact')]","//section[starts-with(@class,'contact-us')]"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)