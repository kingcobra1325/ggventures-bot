from spider_template import GGVenturesSpider


class Esp0019Spider(GGVenturesSpider):
    name = "esp_0019"
    start_urls = ["https://en.eserp.com/contact-us/"]
    country = "Spain"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universidad Carlos III de Madrid,Department of Business Administration"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Logo_UC3M.svg/1200px-Logo_UC3M.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://business.uc3m.es/en/seminarsexternal"

    university_contact_info_xpath = "//span[@class='foot-contacto']/../../.."
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
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h3/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=True):
            # for link in self.events_list(event_links_xpath="//h3/a"):
            for link in self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.presence_of_all_elements_located((self.Mth.By.XPATH,"//div[@class='noticia-blog faculty-img']"))):
                # self.getter.get(link)
                # if self.unique_event_checker(url_substring=["https://www.tut.ac.za/whats-on/events/"]):
                    
                self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = response.url
                
                
                item_data['event_name'] = self.Mth.WebDriverWait(link, 10).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,".//div[starts-with(@class,'titulo-seminario')]"))).text
                item_data['event_desc'] = self.scrape_xpath(xpath_list=[".//div[@class='details']"],enable_desc_image=True,error_when_none=False,driver=link,wait_time=5)
                item_data['event_date'] = link.find_element(self.Mth.By.XPATH,"./div").get_attribute('textContent')
                item_data['event_time'] = link.find_element(self.Mth.By.XPATH,".//div[@style='font-size: 13px;'][2]").get_attribute('textContent')

# 
                yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
