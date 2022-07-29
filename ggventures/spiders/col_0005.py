
from spider_template import GGVenturesSpider


class Col0005Spider(GGVenturesSpider):
    name = 'col_0005'
    start_urls = ['https://www.uexternado.edu.co/administracion-de-empresas/directorio/']
    country = "Colombia"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Universidad Externado de Colombia,Facultad de Administración de Empresas"
    static_logo = "https://www.uexternado.edu.co/wp-content/uploads/2019/04/facultad-adminsitracion-empresas-1.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uexternado.edu.co/lista-de-eventos/"

    university_contact_info_xpath = "//aside[@class='informacion-facultad']"
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
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[@class='h5']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//h3[@class='h5']/a"):
                self.getter.get(f"{link}")
                if self.unique_event_checker(url_substring=['https://www.uexternado.edu.co/evento/']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_link'] = link
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//main//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//main/article"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='submodulo-evento']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='submodulo-evento']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)
                    
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
