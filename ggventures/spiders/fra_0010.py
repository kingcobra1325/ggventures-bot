from spider_template import GGVenturesSpider


class Fra0010Spider(GGVenturesSpider):
    name = "fra_0010"
    start_urls = ["https://www.esc-clermont.fr/en/"]
    country = "France"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "ESC Clermont"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/en/e/ee/ESC_Clermont_Business_School_logo.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.esc-clermont.fr/en/events/"

    university_contact_info_xpath = "//div[contains(@class,'col contact-col')]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            self.ClickMore(click_xpath="//span[text()='Charger plus d’événements']/..",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//th[@class='next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='posts_wrapper']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.esc-clermont.fr/en/evenement"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='title']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='wrapper']/div"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='date']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='wrapper']/div"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
