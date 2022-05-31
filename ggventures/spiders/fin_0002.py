from spider_template import GGVenturesSpider


class Fin0002Spider(GGVenturesSpider):
    name = 'fin_0002'
    start_urls = ['https://www.aalto.fi/en/aalto-university/aalto-university-contact-information']
    country = "Finland"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "HSE - Helsinki School of Economics,Helsingin Kauppakorkeakoulu"
    static_logo = "https://www.eiasm.org/UserFiles/Image/HSE%20Logo%20Helsinki.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.aalto.fi/en/events"

    university_contact_info_xpath = "//div[@class='aalto-component']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'There are no upcoming events to display at this time.')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[contains(@class,'event-title')]/a",next_page_xpath="//section[contains(@class,'cbs-event-current-pane')]//li[contains(@class,'pager-next')]/a",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//h2[contains(@class,'aalto-listing-row__title')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.aalto.fi/en/events']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1/span"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'text-text')]","//div[@class='aalto-article__ingress']"])
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='single-main-event']//ul"],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='single-main-event']//ul"],method='attr')
                    item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[contains(text(),'CONTACT')]/following-sibling::p"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
