
from spider_template import GGVenturesSpider


class Fin0006Spider(GGVenturesSpider):
    name = 'fin_0006'
    start_urls = ['https://www.aalto.fi/en/aalto-university/aalto-university-contact-information']
    country = "Finland"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Aalto University"
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Aalto_University_logo.svg/1200px-Aalto_University_logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.aalto.fi/en/events"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)            
            # self.check_website_changed(upcoming_events_xpath="//div[@id='eventos']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[contains(@class,'monthview')]//a",next_page_xpath="//li[@class='next']/a",get_next_month=True):
            for link in self.events_list(event_links_xpath="//h2[@class='aalto-listing-row__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['www.aalto.fi/en/events']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='text-text']","//div[@class='aalto-article__ingress']"])
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//h1/following-sibling::div"])
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//h1/following-sibling::div"])
                    item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='field-titulo-informacion-contacto']"],method='attr',error_when_none=True)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
