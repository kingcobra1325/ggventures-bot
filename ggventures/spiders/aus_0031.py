from spider_template import GGVenturesSpider


class Aus0031Spider(GGVenturesSpider):
    name = 'aus_0031'
    start_urls = ["https://www.usc.edu.au/about/structure/schools/school-of-business-and-creative-industries/school-of-business-and-creative-industries-staff#tab-dean-and-head-of-school_12040"]
    country = 'Australia'
    # eventbrite_id = 6073111265
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,410,429]

    static_name = 'University of the Sunshine Coast (USC),Faculty of Business'
    static_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/Logo_of_the_University_of_the_Sunshine_Coast.svg/440px-Logo_of_the_University_of_the_Sunshine_Coast.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.usc.edu.au/community/events"

    university_contact_info_xpath = "//div[@class='tab-content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)            
            # self.check_website_changed(upcoming_events_xpath="//div[@id='eventos']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[@class='four-column']/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//a[text()='MORE']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['usc.edu.au/community/events/']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='text-center']","//h1[contains(@class,'title')]"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//article[@class='grid-area']","//div[contains(@class,'structured-content-rich-text')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event-summary-block'][2]","//time[contains(@data-automation,'event-details-time')]","//div[@class='event-summary-block']/parent::div"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-summary-block']","//time[contains(@data-automation,'event-details-time')]","//div[@class='event-summary-block']/parent::div"],method='attr')
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[contains(@class,'fa-whatsapp')]/parent::div"],error_when_none=False,method='attr')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
