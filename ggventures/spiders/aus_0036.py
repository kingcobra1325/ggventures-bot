
from spider_template import GGVenturesSpider


class Aus0036Spider(GGVenturesSpider):
    name = 'aus_0036'
    start_urls = ['https://www.flinders.edu.au/about/contact-us']
    country = "Australia"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Flinders University"
    static_logo = "https://www.flinders.edu.au/etc.clientlibs/flinders/clientlibs/clientlib-site/resources/images/flinder-logo_white.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://events.flinders.edu.au/home/event-list/"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)            
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'all_posts_event')]//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[contains(@class,'fc-view-month')]//a",next_page_xpath="//span[contains(@class,'ui-corner-right')]",click_next_month=True,run_script=True,wait_after_loading=True):
            for link in self.events_list(event_links_xpath="//div[@id='evcal_list']//div[@class='evo_event_schema']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['events.flinders.edu.au/events']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//span[contains(@class,'evcal_event_title')]"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@itemprop='description']"])
                    item_data['event_date'] = self.Mth.WebDriverWait(self.getter,10).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='evo_event_schema']/script"))).get_attribute('innerHTML')
                    
                    item_data['event_time'] = self.Mth.WebDriverWait(self.getter,10).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='evo_event_schema']/script"))).get_attribute('innerHTML')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
