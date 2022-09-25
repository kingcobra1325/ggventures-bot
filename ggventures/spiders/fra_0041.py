from spider_template import GGVenturesSpider


class Fra0041Spider(GGVenturesSpider):
    name = "fra_0041"
    start_urls = ["https://economie.uca.fr/contacts-et-plan-dacces"]
    country = "France"
    # eventbrite_id = 8447939505
    
    USE_FF_DRIVER = True
    
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Université d'Auvergne Clermont 1,Faculté des Sciences Economiques et de Gestion"
    
    static_logo = "https://spectacle-de-curiosites.msh.uca.fr/static/images/uca.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://economie.uca.fr/actualites"

    university_contact_info_xpath = "//a[@class='pied_banniere__info_telephone ']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[@class='more-button__link']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//a[contains(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//li[@class='avec_vignette']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://economie.uca.fr/actualites/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='description']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[starts-with(text(),'Date')]/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='description']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[@id='block-views-contacts-block']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
