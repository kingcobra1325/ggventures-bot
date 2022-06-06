from spider_template import GGVenturesSpider

class Gbr0015Spider(GGVenturesSpider):
    name = 'gbr_0015'
    start_urls = ['https://www.lancaster.ac.uk/lums/']
    country = 'United Kingdom'
    eventbrite_id = 8447939505
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = ""
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/b/bb/Edinburgh-business-school.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.lancaster.ac.uk/events/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)            
            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'No upcoming')]")
            self.ClickMore(click_xpath="//button[contains(@id,'loadMore')]",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//a[contains(@class,'grid-block')]",next_page_xpath="//a[contains(@aria-label,'Next')]",get_next_month=True):
            for link in self.events_list(event_links_xpath="//a[contains(@class,'event-link')]"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['lancaster.ac.uk']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'event-text')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='time']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='time']"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h2[contains(text(),'Contact Details')]/following-sibling::table"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
