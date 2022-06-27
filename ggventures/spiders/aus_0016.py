from spider_template import GGVenturesSpider


class Aus0016Spider(GGVenturesSpider):
    name = 'aus_0016'
    start_urls = ['https://www.rmit.edu.au/contact']
    country = 'Australia'
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,410,429]

    static_name = "RMIT University,RMIT Business (School of Management)"
    static_logo = "https://i.ytimg.com/vi/nJlQrCGuoz0/maxresdefault.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.rmit.edu.au/events"

    university_contact_info_xpath = "//div[contains(@id,'media-enquiries')]"
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
            for link in self.events_list(event_links_xpath="//h4/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["rmit.edu.au/events"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2[@class='header']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='responsivegrid']/div/div"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'evt-hdr__text__desc')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'evt-hdr__text__desc')]"],method='attr')
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'border-top border-bottom my-1 pb-1')]"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)



