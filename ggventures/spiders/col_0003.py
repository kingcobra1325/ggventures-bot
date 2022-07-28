
from datetime import datetime
from spider_template import GGVenturesSpider


class Col0003Spider(GGVenturesSpider):
    name = 'col_0003'
    start_urls = ['https://administracion.uniandes.edu.co/internacionalizacion/escuela-internacional-de-verano/contact-us/']
    country = "Colombia"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Universidad de Los Andes - UNIANDES"
    static_logo = "https://uniandes.edu.co/sites/default/files/logo-header_0_0.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://eventos.uniandes.edu.co/"

    university_contact_info_xpath = "//section[@data-id='60dc751']/.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//section[contains(@class,'events_views featured_events')]//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            raw_event_times = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//*[text()='Fecha Inicio:']/../..")))
            event_times = [x.text for x in raw_event_times]
            for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//a[@class='jss39']",next_page_xpath="//img[@alt='rig']",get_next_month=True,click_next_month=True,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//div[@class='news_title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://eventos.uniandes.edu.co/",]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    pop_datetime = event_times.pop(0)
                    
                    item_data['event_link'] = link
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='jss20']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//*[text()='Descripción del evento']/.."],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = pop_datetime
                    item_data['event_time'] = pop_datetime
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
