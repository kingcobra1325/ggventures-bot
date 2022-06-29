from spider_template import GGVenturesSpider


class Ven0001Spider(GGVenturesSpider):
    name = 'ven_0001'
    start_urls = ["http://v1.iesa.edu.ve/contactanos/directorio-de-contactos"]
    country = 'Venezuela'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "IESA - Instituto de Estudios Superiores de Administración"
    
    static_logo = "https://www.iesa.edu.ve/images/logo.png?cb=636987889266838096"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.iesa.edu.ve/eventos-y-actividades"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'event-calendar__day-wrap')]//a",next_page_xpath="//span[starts-with(@class,'icon-arrow-calendar')][2]",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@id='blog-list-isotope'][1]//article/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.iesa.edu.ve/eventos-y-actividades/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='page-html']"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//strong[text()='Fecha:']/..","//span[@class='date float-left']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//strong[text()='Horarios:']/../following-sibling::*","//p/parent::div[@class='page-html']"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
