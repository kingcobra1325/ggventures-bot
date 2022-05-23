from spider_template import GGVenturesSpider


class Usa0025Spider(GGVenturesSpider):
    name = 'usa_0025'
    start_urls = ["https://www.fuqua.duke.edu/contact"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Duke University,Fuqua School of Business"
    
    static_logo = "https://www.fuqua.duke.edu/sites/www-prod.fuqua.duke.edu/themes/fuqua_main/images/svg-fuqua-logo-sprite.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.fuqua.duke.edu/virtual-events#!/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='events-card']/a",next_page_xpath="//span[text()='Next Page']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//div[@class='eventCard_links']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://admissions.fuqua.duke.edu/register/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='form_description']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@id='register_date']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@id='register_date']"],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[text()='Contact Info']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
