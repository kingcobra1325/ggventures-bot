from spider_template import GGVenturesSpider


class Rus0015Spider(GGVenturesSpider):
    name = 'rus_0015'
    start_urls = ["https://gsom.spbu.ru/en/about-gsom/contacts/"]
    country = 'Russia'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "St. Petersburg State University,Higher School of Management"
    
    static_logo = "https://gsom.spbu.ru/templates/gsom/img/logo-en.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://gsom.spbu.ru/en/events/"

    university_contact_info_xpath = "//section[@id='u-block-main']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//span[@class='badge']/../a",next_page_xpath="//a[@data-go='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//div[starts-with(@class,'col-12')]//div[starts-with(@class,'fs-16')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://gsom.spbu.ru/en/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["(//section[starts-with(@class,'mb-60')]/div[@class='container'])[2]"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[text()='When:']/ancestor::div[@class='row'][1]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[text()='When:']/ancestor::div[@class='row'][1]"],method='attr')
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h2[text()='Any questions?']/ancestor::section"],method='attr')


                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
