from spider_template import GGVenturesSpider


class Bra0017Spider(GGVenturesSpider):
    name = 'bra_0017'
    start_urls = ["https://www.mackenzie.br/universidade/unidades-academicas/ccsa/contatos"]
    country = 'Brazil'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universidade Presbitariana Mackenzie,Centro de Ciências Sociais e Aplicadas - CCSA"
    
    static_logo = "https://www.mackenzie.br/fileadmin/CONFIGURACOES/DEFAULT_21/Resources/Public/Template/img/logo/universidade_mack_v2.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.mackenzie.br/noticias/eventos"

    university_contact_info_xpath = "//div[@class='entry-content']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//article[starts-with(@class,'col-md-12')]/h2/a",next_page_xpath="//tr[@class='calendar-box-header']/th[3]/a",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//article//span[text()='Eventos']//ancestor::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.mackenzie.br/noticias/artigo"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@itemprop='articleBody']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[contains(text(),'Data')] | //h4[contains(text(),'Data')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[contains(text(),'Data')] | //h4[contains(text(),'Data')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
