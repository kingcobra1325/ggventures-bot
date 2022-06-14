from spider_template import GGVenturesSpider
from datetime import datetime


class Mys0006Spider(GGVenturesSpider):
    name = 'mys_0006'
    start_urls = ['https://fpe.um.edu.my/contact-us']
    country = "Malaysia"
    # eventbrite_id = 6552000185
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Malaya,Faculty of Business and Accountancy"
    static_logo = "https://fpe.um.edu.my/images/img-logo-UM.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://portal.um.edu.my/eCalendar/production/json_events.php"

    university_contact_info_xpath = "//div[@class='layoutmanager']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def get_api_events(self,url):
        result = []
        url = url
        payload = ""
        response = self.request_api_call(url=url)
        for event in response:
            event_date = datetime.strptime(event['start'],"%Y-%m-%d")
            if event_date >= datetime.utcnow():
                result.append(event)
            else:
                continue
        self.logger.debug(f"Number of Events: {len(result)}")
        return result

    def parse_code(self,response):
        try:
        ####################
            for event in self.get_api_events(response.url):
                link = "https://portal.um.edu.my/doc/emajlis/"+event['uploadfile']
                self.Func.print_log(f"Currently scraping --> {link}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = link

                item_data['event_name'] = event['title']
                item_data['event_desc'] = event['desc']
                item_data['event_date'] = "\n".join([event['start'],event['end']])
                item_data['event_time'] = "\n".join([event['start'],event['end']])
                # item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                item_data['startups_contact_info'] = "\n".join([event['org_tel'],event['org_emel']])
                item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
