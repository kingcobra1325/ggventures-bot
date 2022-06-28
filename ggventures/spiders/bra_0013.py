from spider_template import GGVenturesSpider


class Bra0013Spider(GGVenturesSpider):
    name = 'bra_0013'
    start_urls = ["https://www.ufpe.br/agencia/fale-conosco"]
    country = 'Brazil'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "UFPE - Universidade Federal de Pernambuco,Departamento de Ciências Administrativas"
    
    static_logo = "https://www.ufpe.br/image/company_logo?img_id=20911&t=1651170929801"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ufpe.br/eventos?p_p_id=101_INSTANCE_PcyqOMdAIP1f&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-3&p_p_col_count=1"

    university_contact_info_xpath = "//table"
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
            
            for link in self.multi_event_pages(num_of_pages=5,event_links_xpath="//h4[@class='list-events__title']/a",next_page_xpath="//li[not(contains(@class,'disabled'))]/a[text()=' Último → ']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            # for link in self.events_list(event_links_xpath="//h4[@class='list-events__title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.ufpe.br/eventos"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h3[@class='header-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='asset-content']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='asset-content']//p[not(@*)]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='asset-content']//p[not(@*)]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Serviço')]/.."],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
