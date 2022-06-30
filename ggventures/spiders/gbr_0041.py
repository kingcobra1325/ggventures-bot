from spider_template import GGVenturesSpider

class Gbr0041Spider(GGVenturesSpider):
    name = 'gbr_0041'
    country = 'United Kingdom'
    start_urls = ["https://www.sbs.ox.ac.uk/about-us/contact-us"]
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Oxford,Said Business School"
    
    static_logo = "https://globalnetwork.io/sites/default/files/styles/member_school_logo_main_page/public/2019-09/SBS_LOGO_RGB_KEYLINE.png?itok=hmsskXBw"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.sbs.ox.ac.uk/events"

    university_contact_info_xpath = "//div[@class='content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='There are no forthcoming events currently listed. Please see the archive for past events.']")
            
            # self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//a[contains(@class,'teal')]",next_page_xpath="//a[@title='Page ›']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//h3[starts-with(@class,'finder')]/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["sbs.ox.ac.uk/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1[@class='article__heading']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[starts-with(@class,'col-sm-8')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//h4[@class='article__meta__heading']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[@class='article__meta__text']"],method='attr',error_when_none=False)
                    
                    # item_data['event_date'] = self.get_datetime_attributes("//time[@itemprop='startDate']",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time[@itemprop='startDate']",'datetime')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[contains(text(),'Contact')]/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)