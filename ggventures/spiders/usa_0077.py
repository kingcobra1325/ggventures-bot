from spider_template import GGVenturesSpider


class Usa0077Spider(GGVenturesSpider):
    name = 'usa_0077'
    start_urls = ["https://www.smeal.psu.edu/about-smeal/penn-state-smeal-contact-information"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The Pennsylvania State University,Smeal College of Business Administration"
    
    static_logo = "https://sc247.s3.amazonaws.com/images/company/penn-state-smeal-college.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.smeal.psu.edu/events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@name='trumba.spud.3.iframe']")))
            
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            for link in self.events_list(event_links_xpath="//span[@class='twDescription']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.smeal.psu.edu/events"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    self.switch_iframe(iframe_driver=self.getter,iframe_xpath="//iframe[@name='trumba.spud.3.iframe']",error_when_none=False)
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//span[@class='twEDDescription']/.."],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//td[@class='twEDContentCell']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[@class='twEDStartEndRange']/.."],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[@class='twEDStartEndRange']/.."],method='attr',error_when_none=False)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='contact']"],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
