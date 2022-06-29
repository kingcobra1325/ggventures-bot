from spider_template import GGVenturesSpider


class Usa0091Spider(GGVenturesSpider):
    name = 'usa_0091'
    start_urls = ["https://www.mccombs.utexas.edu/about/contact/"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "The University of Texas at Austin,McCombs School of Business"
    
    static_logo = "https://www.mccombs.utexas.edu/media/mccombs-website/site-assets/images/utilityNav-logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.mccombs.utexas.edu/news-and-events/events/"

    university_contact_info_xpath = "//body"
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
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//div[@class='htmlText']"):
                    
                self.Func.print_log(f"Currently scraping --> {self.driver.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = self.driver.current_url
                
                item_data['event_name'] = link.find_element(self.Mth.By.XPATH,"./h2").text
                item_data['event_desc'] = link.find_element(self.Mth.By.XPATH,"./p").text
                item_data['event_date'] = link.find_element(self.Mth.By.XPATH,"./h3").text
                try:
                    item_data['event_time'] = link.find_element(self.Mth.By.XPATH,".//strong[contains(text(),'Time')]").text
                except self.Exc.NoSuchElementException as e:
                    self.logger.debug(f"Error |{e}|. Skipping XPATH...")

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
