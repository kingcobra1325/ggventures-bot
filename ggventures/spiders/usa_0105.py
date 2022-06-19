from spider_template import GGVenturesSpider

class Usa0105Spider(GGVenturesSpider):
    name = 'usa_0105'
    country = 'US'
    start_urls = ["https://www.anderson.ucla.edu/degrees/full-time-mba/meet-our-team/contact-us"]
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of California - Irvine,The Paul Merage School of Business"
    
    static_logo = "https://merage.uci.edu/_files/images/logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://api.eventcalendarapp.com/events?id=5973"

    university_contact_info_xpath = "//div[@id='region--content']//div[@class='container']/div[2]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    num_of_events = 50

    def get_api_events(self,url):
        result = []
        url = url
        page = 0
        payload = ""
        params={}
        # while True:
        #     params = {"page":page}
        #     response = self.request_api_call(url=url,params=params)
        #     response_events = response['page']['content']
        #     page+=1
        #     if response_events:
        #         self.logger.debug(f"API Events: {response_events}")
        #         result.extend(response_events)
        #     else:
        #         break
        result = self.request_api_call(url=url,params=params)["events"]
        self.logger.debug(f"All API Events: {result}")
        self.logger.debug(f"Number of Events: {len(result)}")
        return result


    def parse_code(self,response):
        try:
        ####################
            scraped_events = 0

            no_new_events = True
            
            for event in self.get_api_events(response.url):
                self.logger.debug("Event Detected. Sending Emails...")
                self.Mth.website_changed(self.name,self.static_name)
                no_new_events = False
                break
            
            if no_new_events:
                self.logger.debug("No Events found...")

                
                # link = "https://merage.uci.edu/events/"+event['url']
                # self.Func.print_log(f"Currently scraping --> {link}","info")

                # item_data = self.item_data_empty.copy()

                # start_timestamp = int(event['start'])/1000
                # start_date = self.Mth.datetime.fromtimestamp(start_timestamp)

                # end_timestamp = int(event['end'])/1000
                # end_date = self.Mth.datetime.fromtimestamp(end_timestamp)

                # if self.Mth.datetime.utcnow() > start_date:
                #     self.logger.debug("Event has already passed. Skipping...")
                #     continue
                
                # self.getter.get(link)
                
                # item_data['event_link'] = link

                # item_data['event_name'] = event['title']
                # item_data['event_desc'] = event['description']
                # item_data['event_date'] = "\n".join([start_date.strftime("%B %d, %Y %I:%M:%S %p"),end_date.strftime("%B %d, %Y %I:%M:%S %p")])
                # item_data['event_time'] = "\n".join([start_date.strftime("%B %d, %Y %I:%M:%S %p"),end_date.strftime("%B %d, %Y %I:%M:%S %p")])
                # # item_data['startups_link'] = event['onlineJoinUrl']
                # # item_data['startups_name'] = ''
                # # item_data['startups_contact_info'] = ''
                # item_data['event_link'] = link

                # yield self.load_item(item_data=item_data,item_selector=link)

                # scraped_events+=1
                # if scraped_events >= self.num_of_events:
                #     self.logger.debug("Scraped Events Limit Reached...")
                #     break

        ####################
        except Exception as e:
            self.exception_handler(e)
