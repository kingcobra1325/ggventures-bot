from binaries import Load_Driver
from spider_template import GGVenturesSpider


class Kor0004Spider(GGVenturesSpider):
    name = 'kor_0004'
    start_urls = ["https://www.ewha.ac.kr/ewhaen/intro/location.do"]
    country = 'South Korea'
    # eventbrite_id = 6221361805

    handle_httpstatus_list = [301,302,403,404,400]

    static_name = "Ewha Woman's University,School of Business"
    
    static_logo = "https://www.ewha.ac.kr/_res/ewhaen/img/common/img-logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.ewha.ac.kr/app/board/calendar/getEventMonthData2.do"

    university_contact_info_xpath = "//div[@class='footer-inner']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True


    def get_api_events(self,url):
        result = []
        url = url
        page = 0
        payload = ""
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
        params = {'boardNo':'66','siteLng':'en'}
        response = self.request_api_call(url=url,params=params)
        result = response['data']
        self.logger.debug(f"Number of Events: {len(result)}")
        return result


    def parse_code(self,response):
        try:
        ####################
            for event in self.get_api_events(response.url):
                link = f"https://www.ewha.ac.kr/ewhaen/news/event.do?mode=view&articleNo={event['articleNo']}"
                self.getter.get(link)
                self.Func.print_log(f"Currently scraping --> {link}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = link

                item_data['event_name'] = event['title']
                # item_data['event_desc'] = event['body']
                item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='b-content-box']"],method='attr',enable_desc_image=True)
                item_data['event_date'] = "\n".join([event['start'],event['end']])
                item_data['event_time'] = "\n".join([event['start'],event['end']])
                # item_data['startups_link'] = event['onlineJoinUrl']
                # item_data['startups_name'] = ''
                # item_data['startups_contact_info'] = ''
                item_data['event_link'] = link

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)

