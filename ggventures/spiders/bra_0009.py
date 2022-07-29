from spider_template import GGVenturesSpider


class Bra0009Spider(GGVenturesSpider):
    name = "bra_0009"
    start_urls = ["https://www.ibmec.br/sp/fale-conosco"]
    country = "Brazil"
    # eventbrite_id = 12790629019

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "IBMEC São Paulo"
    
    static_logo = "https://s3.amazonaws.com/public-cdn.ibmec.br/portalibmec-content/public/logo/logo-ibmec-topo-sp.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://blog.ibmec.br/tag/empreendedorismo/"

    university_contact_info_xpath = "//div[@class='pane-content']"
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
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2[@class='entry-title']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//span[contains(text(),'More info')]/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://blog.ibmec.br"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='entry-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='entry-content']"],enable_desc_image=True,error_when_none=False,method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Data')]/..","//li[contains(text(),'Dia')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Horário')]/..","//li[contains(text(),'Horário')]/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'c-contact-card')]"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
