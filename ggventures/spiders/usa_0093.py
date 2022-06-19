from calendar import month
from spider_template import GGVenturesSpider
from datetime import datetime, timedelta
import requests

class Usa0079Spider(GGVenturesSpider):
    name = 'usa_0093'
    country = 'US'
    start_urls = ["https://business.utsa.edu/maps-directions/"]
    
    # eventbrite_id = 6221361805
    handle_httpstatus_list = [301,302,400,403,404]

    static_name = "The University of Texas at San Antonio (UTSA),College of Business"
    
    static_logo = "https://business.utsa.edu/wp-content/uploads/2017/11/global-header-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://business.utsa.edu/calendar/"

    university_contact_info_xpath = "//main"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def get_api_events(self,url):
        result = []
        url = url
        num_of_months = 0
        params = {}
        current_date = datetime.utcnow()
        while True:
            parsed_events = []
            payload = f"action=the_ajax_hook&direction=next&shortcode[show_repeats]=no&evodata[cyear]={current_date.year}&evodata[cmonth]={current_date.month}"
            self.logger.debug(f"PAYLOAD:|||{payload}|||")
            # response = self.request_api_call(url=url,params=params,payload=payload,method="POST")
            headersList = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/x-www-form-urlencoded" 
            }
            response = requests.request("POST", url, data=payload,headers=headersList).json()
            # self.logger.debug(f"RESPONSE:|||{response}|||")
            response_events = response["eventList"]
            if response_events:
                html_response = self.convert_str_to_html(response["content"])
                for event in response_events:
                    self.logger.debug(f"RESPONSE: |{event}|")
                    start_date = datetime.fromtimestamp(int(event["event_start_unix"])).strftime("%m/%d/%Y %I:%M:%S %p")
                    end_date = datetime.fromtimestamp(int(event["event_end_unix"])).strftime("%m/%d/%Y %I:%M:%S %p")
                    event_id = event["event_id"]
                    event_dict = {
                                    "id" : event_id,
                                    "link" : html_response.xpath(f"//div[contains(@id,'{event_id}')]//a[@class='evo_ics_nCal']/@href").get(),
                                    "title" : event["event_title"],
                                    "datetime" : f"{start_date}-{end_date}",
                                    "desc" : html_response.xpath(f"string(//div[contains(@id,'{event_id}')]//div[@itemprop='description'])").get(),
                                }
                    parsed_events.append(event_dict)
                self.logger.debug(f"API Events: {parsed_events}")
                result.extend(parsed_events)
            else:
                break
            if num_of_months >= 6:
                break
            else:
                num_of_months+=1
                current_date+=timedelta(days=31)
        self.logger.debug(f"Number of Events: {len(result)}")
        return result

    def parse_code(self,response):
        try:
        ####################
            # height = self.driver.execute_script("return document.body.scrollHeight")
            # self.Mth.WebScroller(self.driver,height)
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.1.iframe']")))
            for event in self.get_api_events("https://business.utsa.edu/wp-admin/admin-ajax.php"):
                link = event["link"]
                self.Func.print_log(f"Currently scraping --> {link}","info")

                item_data = self.item_data_empty.copy()

                item_data['event_name'] = event['title']
                item_data['event_desc'] = event["desc"]
                item_data['event_date'] = event["datetime"]
                item_data['event_time'] = event["datetime"]
                # item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                # item_data['startups_contact_info'] = ''
                item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

            
        ####################
        except Exception as e:
            self.exception_handler(e)