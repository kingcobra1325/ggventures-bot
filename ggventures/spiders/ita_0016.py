from spider_template import GGVenturesSpider


class Ita0016Spider(GGVenturesSpider):
    name = "ita_0016"
    start_urls = ["https://www.unipa.it/faq"]
    country = "Italy"
    # eventbrite_id = 14858065474
# 
    handle_httpstatus_list = [301,302,403,404]

    static_name = "Università degli studi di Palermo,Facoltà di Economia"
    
    static_logo = "https://www.unipa.it/.content/immagini/hp_new/xlogo-unipa-rainbow2.png.pagespeed.ic.72uQtXYhRo.webp"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.unipa.it/dipartimenti/seas/struttura/eventi.html"

    university_contact_info_xpath = "//span[starts-with(@class,'adr-group')]/../.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//span[@class='field-content']/a | //td[@class='multi-day']//a",next_page_xpath="//li[@class='date-next']/a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//h3[@class='title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.unipa.it/dipartimenti/seas/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='page-content']//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='readcontent']",],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='readcontent']"],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='readcontent']"],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//p[@class='contact-item']/.."],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
