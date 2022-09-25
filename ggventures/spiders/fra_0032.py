from spider_template import GGVenturesSpider


class Fra0032Spider(GGVenturesSpider):
    name = "fra_0032"
    start_urls = ["https://www.imt-bs.eu/contacts-acces/"]
    country = "France"
    # eventbrite_id = 8447939505
# 
    handle_httpstatus_list = [301,302,403,404]

    static_name = "INT Management"
    
    static_logo = "https://www.imt-bs.eu/wp-content/uploads/2021/08/LOGO_IMT-BS_RVB-160-px.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.imt-bs.eu/en/news/calendar-of-events/"

    university_contact_info_xpath = "//h2[text()='Nous contacter']/../../.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
            event_times = self.multi_event_dates(date_xpath="//div[@class='elementor-post__excerpt']")
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3[@class='elementor-post__title']/a",next_page_xpath="//a[@class='page-numbers next']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[starts-with(@class,'widgetbox')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.imt-bs.eu/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    datetime = event_times.pop(0)
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='elementor-widget-container']/p/.."],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='elementor-widget-container']/p"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['event_date'] = datetime
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-item__icon']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
