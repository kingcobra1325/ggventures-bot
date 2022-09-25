from spider_template import GGVenturesSpider


class Fra0026Spider(GGVenturesSpider):
    name = "fra_0026"
    start_urls = ["https://en.grenoble-em.com/contact-us"]
    country = "France"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Grenoble Ecole de Management"
    
    static_logo = "https://en.grenoble-em.com/sites/all/themes/gem_main/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://en.grenoble-em.com/upcoming-events"

    university_contact_info_xpath = "//div[@class='field-items']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//button[text()='View More']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//th[@class='next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//a[@class='read-more']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://en.grenoble-em.com/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='page-header']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='main']","//section[@id='block-system-main']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='block-date']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='block-date']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
