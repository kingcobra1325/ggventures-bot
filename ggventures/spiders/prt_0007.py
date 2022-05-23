
from spider_template import GGVenturesSpider

class Prt0007Spider(GGVenturesSpider):
    name = 'prt_0007'
    start_urls = ['https://www.uc.pt/en/sobrenos/localizacao_contactos/servicosapoioaccaosocial']
    country = "Portugal"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "University of Coimbra, Polytechnic Institute  of Coimbra"
    static_logo = "https://e7.pngegg.com/pngimages/468/266/png-clipart-university-of-coimbra-utrecht-university-higher-education-research-and-innovation-for-sustainability-universidad-text-logo-thumbnail.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://noticias.uc.pt/artigos/eventos"

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
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[@class='four-column']/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'grid-flow-row')]/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['noticias.uc.pt/artigos']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='c_text']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='c_text']"])
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='c_text']"])
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'vuw-contact')]"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
