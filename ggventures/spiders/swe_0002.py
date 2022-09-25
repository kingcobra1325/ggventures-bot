from spider_template import GGVenturesSpider


class Swe0002Spider(GGVenturesSpider):
    name = "swe_0002"
    start_urls = ["https://ju.se/en/about-us/contact.html#showmore-Contactinformation"]
    country = "Sweden"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Göteborg University,School of Business Economics and Law"
    
    static_logo = "https://ju.se/webapp-files/juwebstyles/0.0.229/images/logo/ju_logo_white.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ju.se/en/study-at-ju/meet-us.html"

    university_contact_info_xpath = "//h2[text()='Jönköping University Foundation']/../../.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='calenderitem']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://ju.se/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='heading-1']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["(//div[starts-with(@class,'pagecontent')])[2]"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='normal']/text()[contains(.,'Date')]/ancestor::p","//p[@class='normal']/strong[starts-with(text(),'When:')]/../following-sibling::p","//p[@class='normal']/text()[contains(.,'When:')]/ancestor::p","//h3[@id='h-When']/following-sibling::p","//p[starts-with(text(),'Time:')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='normal']/text()[contains(.,'Time:')]/ancestor::p","//p[@class='normal']/strong[starts-with(text(),'When:')]/../following-sibling::p","//p[@class='normal']/text()[contains(.,'When:')]/ancestor::p","//h3[@id='h-When']/following-sibling::p","//p[@class='normal']//*[starts-with(text(),'Time:')]","//p[starts-with(text(),'Time:')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='article-coordination-info']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
