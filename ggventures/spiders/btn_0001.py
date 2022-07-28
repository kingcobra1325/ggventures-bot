
from spider_template import GGVenturesSpider


class Btn0001Spider(GGVenturesSpider):
    name = 'btn_0001'
    start_urls = ['http://www.rim.edu.bt/']
    country = "Bhutan"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Royal Institute of Management"
    static_logo = "http://www.rim.edu.bt/wp-content/uploads/2021/03/rim-header2021-v01-1.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "http://www.rim.edu.bt/?page_id=9268"

    university_contact_info_xpath = "//strong[text()='POSTAL ADDRESS']/../.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[@rel='next']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@class='item-details']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["http://www.rim.edu.bt/?p"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='entry-title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='td-post-content']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='td-post-content']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='td-post-content']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
