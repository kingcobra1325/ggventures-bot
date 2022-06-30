from spider_template import GGVenturesSpider
from datetime import datetime, timedelta
import requests

class Bra0008Spider(GGVenturesSpider):
    name = 'bra_0008'
    start_urls = ["https://www.fdc.org.br/fale-conosco"]
    country = 'Brazil'
    # eventbrite_id = 6221361805

    handle_httpstatus_list = [301,302,403,404]

    static_name = "Fundação Dom Cabral"
    
    static_logo = "https://www.fdc.org.br/Style%20Library/FDC/img/logoFDC.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.fdc.org.br/_layouts/15/FDC.Portal.Sharepoint/WebMethod.aspx/GetItensCalendario"

    university_contact_info_xpath = "//a[@class='fdc-telefone']/.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

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
                "mes":current_date.month,
                "ano":current_date.year
            }            
            # response = self.request_api_call(url=url,params=params,payload=payload,method="POST")
            headersList = {
            "Accept": "*/*",
            "content-type": "application/json; charset=utf-8" 
            }
            response = requests.request("GET", url=url, params=params,headers=headersList).json()
            # self.logger.debug(f"RESPONSE:|||{response}|||")
            response_events = response["d"]
            if response_events:
                html_response = self.convert_str_to_html(response_events)
                links = html_response.xpath(f"//a[@class='more-with-arrow']/@href").getall()
                result.extend(links)
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
            # height = self.driver.execute_script("return document.body.scrollHeight")
            # self.Mth.WebScroller(self.driver,height)
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.1.iframe']")))
            for event in self.get_api_events(response.url):
                link = f"https://www.fdc.org.br{event}"
                self.getter.get(link)
                self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                item_data = self.item_data_empty.copy()

                item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@Class='fdc-box-titulo']"],method='attr')
                item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='mdl-grid']//div[contains(@id,'PlaceHolderMain')]","//section//div[@class='mdl-grid']"],method='attr')
                item_data['event_date'] = self.scrape_xpath(xpath_list=["//b[contains(text(),'Date')]/..","//div[@class='turma-info-container']"],method='attr',error_when_none=False)
                item_data['event_time'] = self.scrape_xpath(xpath_list=["//b[contains(text(),'Time')]/..","//div[@class='turma-info-container']"],method='attr',error_when_none=False)
                # item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                # item_data['startups_contact_info'] = ''
                item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

            
        ####################
        except Exception as e:
            self.exception_handler(e)