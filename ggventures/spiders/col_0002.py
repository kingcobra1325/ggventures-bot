
from spider_template import GGVenturesSpider


class Col0002Spider(GGVenturesSpider):
    name = 'col_0002'
    start_urls = ['http://https://www.udea.edu.co/wps/portal/udea/web/inicio/unidades-academicas/ciencias-economicas/']
    country = "Colombia"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Universidad de Antioquia,Facultad de Ciencias Económicas"
    static_logo = "https://www.udea.edu.co/wps/wcm/connect/udea/3ef4bbd1-4ae7-4c87-b843-685c6f017501/logo-udea.png?MOD=AJPERES&CACHEID=ROOTWORKSPACE.Z18_L8L8H8C0LODDC0A6SSS2AD2GO4-3ef4bbd1-4ae7-4c87-b843-685c6f017501-lr.XbEn"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://cea.javeriana.edu.co/noticias-y-eventos"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            upcoming_button = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.element_to_be_clickable((self.Mth.By.XPATH,"//a[contains(text(),'Following')]")))
            upcoming_button.click()

            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//table//h3/a",next_page_xpath="//li[@class='tribe-events-nav-next']/a",get_next_month=True):
            for link in self.events_list(event_links_xpath="//h3/a"):
                self.getter.get(f"{link}")
                if self.unique_event_checker(url_substring=['eventos.fen.uchile.cl/ver']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='cuerpo']/div[@class='cuerpo']"],error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='ficha']"])
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='ficha']"])

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
