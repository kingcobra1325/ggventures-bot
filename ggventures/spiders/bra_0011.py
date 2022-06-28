from spider_template import GGVenturesSpider


class Bra0011Spider(GGVenturesSpider):
    name = "bra_0011"
    start_urls = ["https://iag.puc-rio.br/en/contact/"]
    country = "Brazil"
    # eventbrite_id = 12790629019

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "PUC-Rio (Pontifícia Universidad Católica),IAG - Instituto de Administração e Gerência"
    
    static_logo = "https://site-stg.iag.puc-rio.br/wp-content/uploads/2020/05/logo_iag_puc_rio@1x.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://iag.puc-rio.br/eventos/"

    university_contact_info_xpath = "(//div[starts-with(@class,'fusion-builder-row')])[3]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h2[@class='entry-title']/a",next_page_xpath="//a[starts-with(@class,'next')]",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            raw_event_names = self.Mth.WebDriverWait(self.driver,40).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//h2/a")))
            event_names = [x.text for x in raw_event_names]
            for link in self.events_list(event_links_xpath="//h2/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://iag.puc-rio.br/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = event_names.pop(0)
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='post-content']","//div[@class='entry-content']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[contains(text(),'Data')] | //h4[contains(text(),'Data')]"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[contains(text(),'Data')] | //h4[contains(text(),'Data')]"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["(//div[@class='fusion-text']//h4//strong)[last()]"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
