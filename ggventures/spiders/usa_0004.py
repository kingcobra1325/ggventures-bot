from cgi import parse_multipart
from xml.etree.ElementPath import xpath_tokenizer
from spider_template import GGVenturesSpider
from datetime import datetime, timedelta
import ast
import requests

class Usa0004Spider(GGVenturesSpider):
    name = 'usa_0004'
    start_urls = ["https://www.babson.edu/contact-babson/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Babson College"
    
    static_logo = "https://www.auburn.edu/template/2022/_assets/images/logos/auburn/formal_horiz/onecolor_white/auburn_formal_h_onecolor_white_web.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.babson.edu/about/events/"

    university_contact_info_xpath = "//div[@id='section-content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = False
    
    def get_api_events(self,url,max_events=30):
        result = []
        url = url
        params = {}
        current_date = datetime.utcnow()
        current_page = 1
        
        while True:
            params = {
                "day" : current_date.day,
                "month" : current_date.month,
                "year" : current_date.year,
                "page" : current_page
            }
            
            response = requests.request("GET", url=url, params=params)
            response_parsed = response.text
            
            if response_parsed:
                html_response = self.convert_str_to_html(response_parsed)
                event_divs = html_response.xpath("//li[starts-with(@class,'event-item')]").getall()
                self.Func.print_log(f"List selector is {event_divs}")
                for event_link in event_divs:
                    event_link_parsed = self.convert_str_to_html(event_link)
                    result.append(
                        {
                            "Event Link" : event_link_parsed.xpath("//a[@class='find-out-more']/@href").get(),
                            "Event Name" : event_link_parsed.xpath("//p[@class='title']/text()").get(),
                            "Event Description" : "".join(event_link_parsed.xpath("//div[@class='image']//*/text()").getall()),
                            # "Event Date" : event_link_parsed.xpath("//div[@class='event-date-box']/*/text()").get(),
                            "Event Date" : "".join(event_link_parsed.xpath("//div[@class='event-date-box']//*/text()").getall()),
                            # "Event Time" : event_link_parsed.xpath("//span[@class='fa fa-clock']/*/text()").get(),
                            "Event Time" : "".join(event_link_parsed.xpath("//span[@class='fa fa-clock']//*/text()").getall()),
                            }
                        )
            
            current_page += 1
            
            if len(result) >= max_events:
                return result
        

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[contains(@class,'teal')]",next_page_xpath="//a[@title='Page ›']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//a[@class='clearfix']"):
            for link in self.get_api_events("https://www.babson.edu/about/events/"):
            # for link in self.driver.find_elements(self.Mth.By.XPATH,"//li[starts-with(@class,'event-item')]"):
                self.logger.info(link)

                self.Func.print_log(f"Link contains {link}")
                
                # self.getter.get(link)                                                                                                                                                                                                                                                                                                                                                                  
                # if self.unique_event_checker(url_substring=["https://web.cvent.com/event/","https://babson-college.secure.force.com/EventRegistration/"]):
                    
                #     self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = link["Event Link"]

                item_data['event_name'] = link["Event Name"]
                
                item_data['event_desc'] = link["Event Description"]
                
                item_data['event_date'] = "".join(link["Event Date"].replace("\n","").replace("\r","").replace("","").split(" "))

                item_data['event_time'] = "".join(link["Event Time"].replace("\n","").replace("\r","").replace("","").split(" "))
                # item_data['event_link'] = self.Mth.WebDriverWait(self.driver,10).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,".//a[@class='find-out-more']"))).get_attribute('textContent')

                # item_data['event_name'] = self.driver.find_element(self.Mth.By.XPATH,".//p[@class='title']").get_attribute('textContent')
                # item_data['event_desc'] = self.driver.find_element(self.Mth.By.XPATH,".//div[@class='image']").text
                # item_data['event_date'] = self.driver.find_element(self.Mth.By.XPATH,".//div[@class='event-date-box']").get_attribute('textContent')
                # item_data['event_time'] = self.driver.find_element(self.Mth.By.XPATH,".//span[@class='fa fa-clock']/..").get_attribute('textContent')
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='em-date']"],method='attr')

                yield self.load_item(item_data=item_data,item_selector=link)
                    


        ####################
        except Exception as e:
            self.exception_handler(e)
