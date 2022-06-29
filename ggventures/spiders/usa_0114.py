from spider_template import GGVenturesSpider
from datetime import datetime, timedelta
import ast
import requests

class Usa0114Spider(GGVenturesSpider):
    name = 'usa_0114'
    start_urls = ["https://www.uidaho.edu/cbe/about/contact-us"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Idaho,College of Business and Economics"
    
    static_logo = "https://www.uidaho.edu/-/media/UIdaho-Responsive/Images/brand-resource-center/toolkit/logo-suites/ui-main-vertical.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.trumba.com/s.aspx"

    university_contact_info_xpath = "//div[starts-with(@class,'obj-sixtysix-thirtythree')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def get_api_events(self,url):
        result = []
        url = url
        num_of_months = 0
        params = {}
        payload = ""
        current_date = datetime.utcnow()
        while True:
            parsed_events = []
            params = {
                "calendar":"university-of-idaho",
                "date": current_date.strftime("%Y%m%d")
            }
            response = requests.request("GET", url=url, params=params)
            response_parsed = response.text.replace("$Trumba.ScriptXmlHttpRequest.requestComplete(","").replace(");","")
            response_json = ast.literal_eval(response_parsed)
            # self.logger.debug(f"RESPONSE:|||{response}|||")
            response_events = response_json["body"]
            if response_events:
                html_response = self.convert_str_to_html(response_events)
                events_ids = html_response.xpath(f"//a[@url.eventid]/@url.eventid").getall()
                events_href = html_response.xpath(f"//a[@url.eventid]/@href").getall()
                for idx, event in enumerate(events_ids):
                    event = event.replace("\\","")
                    event_params = {
                        "calendar":"university-of-idaho",
                        "eventid":event,
                        "view":"event",
                    }
                    event_response = requests.request("GET", url=url, params=event_params)
                    event_response_parsed = event_response.text.replace("$Trumba.ScriptXmlHttpRequest.requestComplete(","").replace(");","")
                    event_response_json = ast.literal_eval(event_response_parsed)
                    event_htmlres = self.convert_str_to_html(event_response_json["body"])
                    result.append({"href":events_href[idx],"event_response":event_htmlres})
                # result.extend(links)
            else:
                break
            if num_of_months >= 6:
                break
            else:
                num_of_months+=1
                current_date+=timedelta(days=31)
        self.logger.debug(f"Events:\n{result}")
        self.logger.debug(f"Number of Events: {len(result)}")
        return result

    def parse_code(self,response):
        try:
        ####################
            for event in self.get_api_events(response.url):
                js_href = event['href'][2:-2]
                self.logger.debug(f"Javascript HREF:|{js_href}|")
                self.getter.execute_script(js_href)
                self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                item_data = self.item_data_empty.copy()

                item_data['event_name'] = event["event_response"].xpath("//div[contains(@role,'heading')]/text()").get()
                item_data['event_desc'] = event["event_response"].xpath("//p[contains(@class,'firstp')]/parent::td/text()").get()
                item_data['event_date'] = event["event_response"].xpath(r"//td[contains(@class,'twEventDetailData\')]/text()").get()
                item_data['event_time'] = event["event_response"].xpath(r"//td[contains(@class,'twEventDetailData\')]/text()").get()
                # item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                # item_data['startups_contact_info'] = ''
                item_data['event_link'] = self.getter.current_url

                yield self.load_item(item_data=item_data,item_selector=self.getter.current_url)

        ####################
        except Exception as e:
            self.exception_handler(e)
