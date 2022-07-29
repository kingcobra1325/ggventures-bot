from spider_template import GGVenturesSpider

class Ken0003Spider(GGVenturesSpider):
    name = 'ken_0003'
    start_urls = ['https://www.usiu.ac.ke/contacts/']
    country = "Kenya"
    # eventbrite_id = 6552000185
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "United States International University"
    static_logo = "https://urbanlive.co.ke/wp-content/uploads/2019/05/USIU-Logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.usiu.ac.ke/includes/calendar/events.all.php"

    university_contact_info_xpath = "//div[@id='articleContent']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    num_of_events = 25

    def get_api_events(self,url):
        result = []
        url = url
        page = 0
        payload = ""
        params={
            "limit":"10",
        }
        result = self.request_api_call(url=url,params=params)
        self.logger.debug(f"All API Events: {result}")
        self.logger.debug(f"Number of Events: {len(result)}")
        return result

    def parse_code(self,response):
        try:
        ####################
            scraped_events = 0
            for event in self.get_api_events(response.url):
                link = "https://www.usiu.ac.ke/"+event['url']
                self.Func.print_log(f"Currently scraping --> {link}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = link

                item_data['event_name'] = event['title']
                item_data['event_desc'] = event['description']
                item_data['event_date'] = event['date']
                item_data['event_time'] = event['time']
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
