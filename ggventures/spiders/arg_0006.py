
from spider_template import GGVenturesSpider
from datetime import datetime, timedelta
import json
import requests


class Arg0006Spider(GGVenturesSpider):
    name = 'arg_0006'
    start_urls = ['https://uca.edu.ar/es/comunicacion-institucional/contacto-de-prensa']
    country = "Argentina"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Universidad Católica de Argentina (UCA),Escuela de Negocios"
    static_logo = "https://uca.edu.ar/assets/img/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://wadmin.uca.edu.ar/api/event/"

    university_contact_info_xpath = "//strong[text()='Natalia Ramil']/../.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    
    def get_api_events(self,incoming_url):
        results = []
        api_url = incoming_url
        
        current_date = datetime.utcnow()
        
        event_count = 0
        
        base_event_url = "https://uca.edu.ar/es/eventos/"
        
        while True:
            api_month = current_date.month
            api_year = current_date.year
            api_params = {
                "locale" : "es",
                "month" : api_month,
                "year" : api_year
            }
            
            
            response = requests.request("GET",url=api_url,params=api_params)
            response_json = json.loads(response.text)
            response_events = response_json["data"][0]["eventArray"]
            
            self.logger.debug("Succesfully requested API...")
            
            if response_events:
                return response_events

                

    def parse_code(self,response):
        try:
        ####################
            # self.check_website_changed(upcoming_events_xpath="//td[contains(@class,'tribe-events-thismonth')]//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'moreListing')]",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True):
            for link in self.get_api_events(response.url):
                parsed_url = "https://uca.edu.ar/es/eventos/" + link["systemTitle"]
                self.getter.get(parsed_url)
                if self.unique_event_checker(url_substring=['uca.edu.ar/es/eventos']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = parsed_url

                    item_data['event_name'] = link["title"]
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='body']/.."],enable_desc_image=True)
                    item_data['event_date'] = f"""{link["startOn"]["date"]}\n{link["endOn"]["date"]}""" 
                    item_data['event_time'] = f"""{link["startOn"]["date"]}\n{link["endOn"]["date"]}""" 
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[text()='Event contact details']/following-sibling::ul"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

    
        
        ####################
        except Exception as e:
            self.exception_handler(e)
