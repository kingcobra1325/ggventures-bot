from spider_template import GGVenturesSpider


class Fra0036Spider(GGVenturesSpider):
    name = "fra_0036"
    start_urls = ["https://www.sciencespo.fr/en/contact-map"]
    country = "France"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Sciences Po Paris"
    
    static_logo = "https://my.vioo.world/wp-content/uploads/2020/12/08234345/sciences_po.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.sciencespo.fr/evenements/"

    university_contact_info_xpath = "//div[starts-with(@class,'internal-page-module')]"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
            
            self.Mth.WebDriverWait(self.driver,50).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//a[@class='push-event-module--linkRoot--DM0wy']")))
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//a[@class='push-event-module--linkRoot--DM0wy']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.sciencespo.fr/fr/evenements/"]):
                    self.Mth.WebDriverWait(self.driver,50).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//div[@class='MuiBox-root css-xi606m']")))
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='MuiBox-root css-xi606m']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='internal-page-module--marginBetweenBlocs--r-G0V' and @style='width: inherit;']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//*[text()='À propos de cet événement']/../../.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//*[text()='À propos de cet événement']/../../.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
