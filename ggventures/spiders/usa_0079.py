from spider_template import GGVenturesSpider


class Usa0079Spider(GGVenturesSpider):
    name = 'usa_0079'
    start_urls = ['https://www.chicagobooth.edu/']
    country = 'US'
    
    # eventbrite_id = 6221361805
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of Chicago, Graduate Business School"
    
    static_logo = "http://www.chicagobooth.edu/boothsitecore/img/chicago_booth_social_thumb.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.chicagobooth.edu/alumni/connect/clubs/chicago/events"

    university_contact_info_xpath = "//main"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # height = self.driver.execute_script("return document.body.scrollHeight")
            # self.Mth.WebScroller(self.driver,height)
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.1.iframe']")))
              
            # for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//h3[@class='event-search-title']/a",next_page_xpath="//a[contains(@title,'Go to next page')]",get_next_month=True,click_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@class='upcoming-events']//div[@class='calContent']//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["chicagobooth.edu"]):

                    # self.Mth.WebDriverWait(self.getter, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.1.iframe']")))
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//span[contains(@id,'EventDetails')]"],method='attr').replace("Event Details","")
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[contains(@id,'DateOfEvent')]/h2"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[contains(@id,'DateOfEvent')]/h2"],method='attr')
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//span[text()='Contact Email']/parent::th/following-sibling::td"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)