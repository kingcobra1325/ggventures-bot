from spider_template import GGVenturesSpider


class Usa0139Spider(GGVenturesSpider):
    name = 'usa_0139'
    start_urls = ["https://eccles.utah.edu/about/connect-with-us/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Utah,David Eccles School of Business"
    
    static_logo = "https://d30i16bbj53pdg.cloudfront.net/wp-content/uploads/2017/12/Eccles_Logo_Header_Final_Desktop.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://eccles.utah.edu/upcoming-events/"

    university_contact_info_xpath = "//h1[text()='Get in Touch']/../../../.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='table-1']"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://calendar.utk.edu/event"]):
            
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//div[@class='table-1']"):
                    
                self.Func.print_log(f"Currently scraping --> {self.driver.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = self.driver.current_url

                item_data['event_name'] = link.find_element(self.Mth.By.XPATH,".//strong").text
                item_data['event_desc'] = link.find_element(self.Mth.By.XPATH,".//tbody").text
                item_data['event_date'] = link.find_element(self.Mth.By.XPATH,".//b[@data-stringify-type='bold']").text
                item_data['event_time'] = link.find_element(self.Mth.By.XPATH,".//tbody").text
                # item_data['startups_contact_info'] = self.driver.find_element(self.Mth.By.XPATH,".//div[@class='table-1']//strong")

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
