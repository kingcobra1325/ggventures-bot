from spider_template import GGVenturesSpider


class Arg0004Spider(GGVenturesSpider):
    name = 'arg_0004'
    start_urls = ["http://www.uade.edu.ar/contacto/"]
    country = "Argentina"
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "UADE - Universidad Argentina de la Empresa,EDDE - Escuela de Dirección de Empresas"
    
    static_logo = "https://www.uade.edu.ar/media/ej0bpn3j/uade_una_gran_universidad.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uade.edu.ar/agenda/"

    university_contact_info_xpath = "//section[@class='richText-section']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//h5[@class='mb-3']/following-sibling::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["www.uade.edu.ar/agenda"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='calendar-text-description']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//ul[contains(@class,'calendar-info-section')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//ul[contains(@class,'calendar-info-section')]"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[text()='Event contact details']/following-sibling::ul"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
