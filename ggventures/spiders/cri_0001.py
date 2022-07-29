
from spider_template import GGVenturesSpider


class Cri0001Spider(GGVenturesSpider):
    name = 'cri_0001'
    start_urls = ['https://www.incae.edu/es/acerca-de-incae/directorio.html']
    country = "Costa Rica"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "INCAE Business School"
    static_logo = "https://www.incae.edu/sites/all/themes/incae/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.incae.edu/es/eventos.html"

    university_contact_info_xpath = "//div[@class='main']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//section[contains(@class,'events_views featured_events')]//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//table//h3/a",next_page_xpath="//li[@class='tribe-events-nav-next']/a",get_next_month=True):
            for link in self.events_list(event_links_xpath="//h2/a"):
                self.getter.get(f"{link}")
                if self.unique_event_checker(url_substring=["https://go.incae.edu/","https://www.incae.edu/es/evento/"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_link'] = link
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'mbr-section-text')]","//div[starts-with(@class,'group-contenido-evento')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//*[contains(text(),'GMT-6')]/ancestor::div[@class='container']","//span[@class='date-display-range']/../.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//*[contains(text(),'GMT-6')]/ancestor::div[@class='container']","//span[@class='date-display-range']/../.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//*[starts-with(text(),'Contacto')]/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
