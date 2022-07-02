from spider_template import GGVenturesSpider


class Esp0025Spider(GGVenturesSpider):
    name = 'esp_0025'
    start_urls = ["https://www.upf.edu/web/universitat/contacte"]
    country = 'Spain'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universitat Pompeu Fabra (UPF) - IDEC"
    
    static_logo = "https://www.upf.edu/upf-2016-theme/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://eventum.upf.edu/search/basic_search.html"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='main']/a",next_page_xpath="//a[text()='Sig >']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='o_card__head']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://eventum.upf.edu/","https://eventum.upf.edu/event_detail/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1","//div[@id='event-header-text']/h3","//div[@id='description-container']/p"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='description-container']","//div[@id='content']/div[2]","//div[@id='event-description-par']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='content-wrapper']","//p[@class='event_date']","//div[@id='description-container']/h2/span","//div[@id='description-container']/p[2]","//div[@id='header']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='content-wrapper']","//p[@class='event_date']","//div[@id='description-container']"],method='attr')
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='phone']"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
