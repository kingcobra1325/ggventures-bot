
from spider_template import GGVenturesSpider


class Uzb0002Spider(GGVenturesSpider):
    name = 'uzb_0002'
    start_urls = ['http://https://www.samdu.uz/en/']
    country = "Uzbekistan"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Samarkand State University Faculty of Economics"
    static_logo = "https://ucu.edu.uy/sites/all/themes/univer/images/logo_es.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ucu.edu.uy/es/agenda"

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
            for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//span[@class='field-content']/a",next_page_xpath="//li[@class='pager-next']/a",get_next_month=True):
                # for link in self.events_list(event_links_xpath="//div[@itemprop='name']/a"):
                self.getter.get(f"{link}")
                if self.unique_event_checker(url_substring=['ucu.edu.uy/es/node']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='title_event_node']/h1[@class='title_event']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'content_event')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'content_event')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'content_event')]"],method='attr')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
