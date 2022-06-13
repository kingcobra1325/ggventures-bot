from spider_template import GGVenturesSpider

class Gbr0050Spider(GGVenturesSpider):
    name = 'gbr_0050'
    country = 'United Kingdom'
    start_urls = ["https://www.wbs.ac.uk/"]
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Warwick,Warwick Business School"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Warwick_Business_School_logo.svg/1711px-Warwick_Business_School_logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://web-api.wbs.ac.uk/events/search"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def get_api_events(self,url):
        result = []
        url = url
        page = 0
        payload = ""
        while True:
            params = {"page":page}
            response = self.request_api_call(url=url,params=params)
            response_events = response['page']['content']
            page+=1
            if response_events:
                self.logger.debug(f"API Events: {response_events}")
                result.extend(response_events)
            else:
                break
        self.logger.debug(f"Number of Events: {len(result)}")
        return result


    def parse_code(self,response):
        try:
        ####################
            for event in self.get_api_events(response.url):
                link = "https://www.wbs.ac.uk/events/view/"+event['id']
                self.Func.print_log(f"Currently scraping --> {link}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = link

                item_data['event_name'] = event['title']
                item_data['event_desc'] = event['body']
                item_data['event_date'] = "\n".join([event['startDate'],event['endDate']])
                item_data['event_time'] = "\n".join([event['startDate'],event['endDate']])
                item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                # item_data['startups_contact_info'] = ''
                item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
