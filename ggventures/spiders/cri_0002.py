
from spider_template import GGVenturesSpider


class Cri0002Spider(GGVenturesSpider):
    name = 'cri_0002'
    start_urls = ['http://www.ean.ucr.ac.cr/contacto']
    country = "Costa Rica"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Universidad de Costa Rica,Escuela de Administración de Negocios"
    static_logo = "http://ean.ucr.ac.cr/sites/all/themes/negocios/img/Universidad-de-Costa-Rica-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "http://www.ean.ucr.ac.cr/noticias"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//article[starts-with(@class,'col-md-12')]/h2/a",next_page_xpath="//tr[@class='calendar-box-header']/th[3]/a",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@class='col-sm-11']//div/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["http://www.ean.ucr.ac.cr/noticias/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link
                    
                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='page-header']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='content']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='content']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='content']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
