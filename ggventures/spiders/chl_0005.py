from spider_template import GGVenturesSpider


class Chl0005Spider(GGVenturesSpider):
    name = "chl_0005"
    start_urls = ["https://www.pucv.cl/pucv/pregrado/facultad-de-ciencias-economicas-y-administrativas"]
    country = "Chile"
    # eventbrite_id = 14858065474

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universidad Católica de Valparaiso,Facultad de Ciencias Economicas y Administrativas"
    
    static_logo = "https://www.pucv.cl/pucv/site/artic/20180109/imag/foto_0000000120180109113142.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.pucv.cl/pucv/site/tax/port/fil_evento/taxport_28___1.html"

    university_contact_info_xpath = "//article[@class='direccion grid-12']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2[@class='card-title']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.pucv.cl/pucv"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='titular']","//h1[@id='#contenido-ppal']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='CUERPO']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//table[@class='tabla-art-evento']","//div[@class='CUERPO']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//table[@class='tabla-art-evento']","//span[@class='hora']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
