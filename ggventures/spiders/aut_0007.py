
from spider_template import GGVenturesSpider


class Aut0007Spider(GGVenturesSpider):
    name = 'aut_0007'
    start_urls = ['https://www.meduniwien.ac.at/web/en/contact/']
    country = "Austria"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Medical University of Vienna"
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/3/36/Meduni-wien.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.meduniwien.ac.at/web/en/about-us/events/"

    university_contact_info_xpath = "(//main//div[@class='container--base'])[2]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)            
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'all_posts_event')]//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[contains(@class,'button-next')]",get_next_month=True):
            for link in self.events_list(event_links_xpath="//a[@class='calendar__title']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['meduniwien.ac.at/web']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='header__headline']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='content']"],method='text')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='event--lead__row']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event--lead__row']"],method='attr',error_when_none=False)

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='wpGeneralWidgetBodyRte']"])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
