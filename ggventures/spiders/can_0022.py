from spider_template import GGVenturesSpider

class Can0022Spider(GGVenturesSpider):
    name = 'can_0022'
    start_urls = ['https://www.rotman.utoronto.ca/']
    country = 'Canada'
    eventbrite_id = 14858065474
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "University of Toronto,Joseph L. Rotman School of Management"
    static_logo = "https://www.rotman.utoronto.ca/-/media/Images/Central/MarketingResources/Rotman-Crest--blackfor-White-backgrounds.png?h=123&w=400&la=en&hash=C7E75A47C12A73AD2C6F148A4EB6C517A55F30A0"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://entrepreneurs.utoronto.ca/events/community-events/"

    university_contact_info_xpath = "//div[contains(@role,'contentinfo')]//td[1]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//div[contains(@class,'cal_load-button')]/button",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[text()='>>']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@data-post-types='event']//h3/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['utoronto.ca/event']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1","//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'wp-block-column--content')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'wp-block-ob-blocks-post-metadata')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'wp-block-ob-blocks-post-metadata')]"],method='attr')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
