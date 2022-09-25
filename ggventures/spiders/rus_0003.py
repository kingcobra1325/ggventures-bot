from spider_template import GGVenturesSpider


class Rus0003Spider(GGVenturesSpider):
    name = "rus_0003"
    start_urls = ["https://eng-ibda.ranepa.ru/about/contacts/"]
    country = "Russia"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "IBS - Institute of Business Studies,Academy of National Economy under the government of RF"
    
    static_logo = "https://eng-ibda.ranepa.ru/local/templates/.default/images/logo_engl.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://eng-ibda.ranepa.ru/"

    university_contact_info_xpath = "//div[@class='about']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[starts-with(@class,'slider__news row')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://eng-ibda.ranepa.ru/about/news/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='header-text__slogan-txt']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='main']"],enable_desc_image=True,error_when_none=True)
                    # item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[text()='Event Summary']/following-sibling::div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[text()='Event Summary']/following-sibling::div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='article-coordination-info']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
