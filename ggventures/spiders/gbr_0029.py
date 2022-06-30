from spider_template import GGVenturesSpider

class Gbr0029Spider(GGVenturesSpider):
    name = 'gbr_0029'
    country = 'United Kingdom'
    start_urls = ["https://www.gla.ac.uk/schools/business/contact/"]
    # eventbrite_id = 18555680858
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "The University of Glasgow,Business School"
    static_logo = "https://ft-bschool-rankings.s3.eu-west-2.amazonaws.com/production/images/f7a938a4-70c2-47a6-a304-664428f01b0e-8841c1ec130f905c348ee707f2d3e5b5"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.gla.ac.uk/schools/business/events/"

    university_contact_info_xpath = "//div[@data-contentname='Contact us']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//div[contains(@class,'cal_load-button')]/button",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[text()='>>']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//a[@Class='tilewraplink']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['gla.ac.uk']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2[@class='unresponsivestyle']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'maincontent')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'maincontent')]//h5","//div[@class='publish-date']","//div[@class='publish-date']/p","//div[@id='article-content']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'maincontent')]//h5","//div[@class='publish-date']","//div[@class='publish-date']/p","//div[@id='article-content']"],method='attr')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)