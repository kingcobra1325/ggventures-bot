
from spider_template import GGVenturesSpider


class Uzb0003Spider(GGVenturesSpider):
    name = 'uzb_0003'
    start_urls = ['https://tfi.uz/en/page/fakultetlar']
    country = "Uzbekistan"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Tashkent Financial Institute"
    static_logo = "https://static.wixstatic.com/media/a8b21d_7bf5d35edc944e58a7047f6b316128ff~mv2.jpg/v1/fill/w_256,h_256,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/e3024bdeee2dee48376c2a76b7147f2f.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://tfi.uz/en/announce/"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@class='col-md-8 col-right']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//span[@class='field-content']/a",next_page_xpath="//li[@class='pager-next']/a",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@class='p10']/a"):
                self.getter.get(f"{link}")
                if self.unique_event_checker(url_substring=['tfi.uz/en/events']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='size18 bold text-center uppercase']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='contents']"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='contents']"])
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='contents']"])

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
