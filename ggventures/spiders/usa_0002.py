from spider_template import GGVenturesSpider


class Usa0002Spider(GGVenturesSpider):
    name = "usa_0002"
    start_urls = ["https://wpcarey.asu.edu/about/contact"]
    country = "US"
    eventbrite_id = 11043978456
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Arizona State University,W. P. Carey School of Business"
    
    static_logo = "https://wpcarey.asu.edu/modules/composer/webspark-module-asu_brand/node_modules/@asu-design-system/component-header/dist/assets/img/arizona-state-university-logo-vertical.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ju.se/en/study-at-ju/meet-us.html"

    university_contact_info_xpath = "//div[@class='block']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        pass
#         try:
#         ####################
#             self.driver.get(response.url)
    
#             # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
#             self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
#             # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
#             for link in self.events_list(event_links_xpath="//div[@class='calenderitem']//a"):
#                 self.getter.get(link)
#                 if self.unique_event_checker(url_substring=["https://ju.se/"]):
                    
#                     self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

#                     item_data = self.item_data_empty.copy()
                    
#                     item_data['event_link'] = link

#                     item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='heading-1']"])
#                     item_data['event_desc'] = self.scrape_xpath(xpath_list=["(//div[starts-with(@class,'pagecontent')])[2]"],method='text',enable_desc_image=True,error_when_none=True)
#                     item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='normal']/text()[contains(.,'Date')]/ancestor::p"],method='attr',error_when_none=False,wait_time=5)
#                     item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='normal']/text()[contains(.,'Time:')]/ancestor::p"],method='attr',error_when_none=False,wait_time=5)
#                     # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='article-coordination-info']"],method='attr',error_when_none=False,wait_time=5)
# # 
#                     yield self.load_item(item_data=item_data,item_selector=link)

#         ###################
#         except Exception as e:
#             self.exception_handler(e)
