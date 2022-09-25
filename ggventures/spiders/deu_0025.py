from spider_template import GGVenturesSpider
from scrapy import Request


class Deu0025Spider(GGVenturesSpider):
    name = 'deu_0025'
    start_urls = ["https://wiso.uni-hohenheim.de/en/contact"]
    country = 'Germany'
    # eventbrite_id = 30819498834
    
    handle_httpstatus_list = [307]
    
    custom_settings = {
        'REDIRECT_ENABLED' : False
    }
    
    static_name = "Universität Hohenheim,Faculty of Business Economics & Social Sciences"
    
    static_logo = "https://www.uni-hohenheim.de/typo3conf/ext/uni_layout/Resources/Public/Images/uni-logo-en.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://wiso.uni-hohenheim.de/en/news"

    university_contact_info_xpath = "//section[@id='content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True


    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
            
            
            raw_event_times = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//div[@class='sub0col']//h3/span")))
            event_times = [x.get_attribute('textContent') for x in raw_event_times]
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='sub0col']//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://wiso.uni-hohenheim.de/en/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link
                    
                    datetime = event_times.pop(0)

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='news-single-item']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = datetime
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[text()='Date']/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
