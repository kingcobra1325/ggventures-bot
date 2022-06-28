from spider_template import GGVenturesSpider


class Deu0016Spider(GGVenturesSpider):
    name = "deu_0016"
    start_urls = ["https://www.rwth-aachen.de/cms/root/Die-RWTH/Kontakt-Anreise/~cxdn/Kontakt/lidx/1/"]
    country = "Germany"
    # eventbrite_id = 14858065474
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "RWTH Aachen University"
    
    static_logo = "https://www.rwth-aachen.de/global/show_picture.asp?id=aaaaaaaaaaagazb"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.rwth-aachen.de/cms/root/Die-RWTH/Aktuell/~ulx/Veranstaltungen/lidx/1/"

    university_contact_info_xpath = "//div[@id='main']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//button[starts-with(@class,'fusion-load-more-button')]",run_script=True)
              
            for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            # for link in self.events_list(event_links_xpath="//h3[@class='eventTeaser-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.hhl.de/event/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='text']/h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='text']","//div[contains(@class,'item-page')]/div[contains(@class,'row')]/div[contains(@class,'col')]"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='text']/h3","//div[contains(@class,'tile__content')]"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='text']/h3","//div[contains(@class,'tile__content')]"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
