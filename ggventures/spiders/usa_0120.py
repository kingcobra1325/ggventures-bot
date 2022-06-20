from spider_template import GGVenturesSpider


class Usa0120Spider(GGVenturesSpider):
    name = 'usa_0120'
    start_urls = ["https://www.isenberg.umass.edu/contact"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Massachusetts - Amherst, Isenberg School of Management"
    
    static_logo = "https://www.isenberg.umass.edu/sites/default/files/styles/shs_mobile_x1_567px/public/2020-00/Isenberg-Logo-in-full_RGB.jpg?itok=ps9VfWLy"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.isenberg.umass.edu/api/events"

    university_contact_info_xpath = "//div[@class='a11y-paragraphs-tabs__section-container']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    num_of_events = 50

    def get_api_events(self,url):
        result = []
        url = url
        page = 0
        payload = ""
        params={}
        while True:
            params = {"page":page,"_format":"json"}
            response = self.request_api_call(url=url,params=params)
            response_events = response['rows']
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
            scraped_events = 0
            
            for event in self.get_api_events(response.url):

                if event['content_url']:
                    link = "https://www.isenberg.umass.edu/"+event['content_url']
                else:
                    link = ""
                # self.Func.print_log(f"Currently scraping --> {link}","info")
                self.Func.print_log(f"Currently scraping --> {event['title']}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = link

                item_data['event_name'] = event['title']
                item_data['event_desc'] = event['summary']
                item_data['event_date'] = event['dates']
                item_data['event_time'] = event['dates']
                # item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                # item_data['startups_contact_info'] = ''
                item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

                scraped_events+=1
                if scraped_events >= self.num_of_events:
                    self.logger.debug("Scraped Events Limit Reached...")
                    break

        ####################
        except Exception as e:
            self.exception_handler(e)
