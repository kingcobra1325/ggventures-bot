from spider_template import GGVenturesSpider


class Tur0002Spider(GGVenturesSpider):
    name = 'tur_0002'
    start_urls = ["https://fbe.emu.edu.tr/en/contact"]
    country = 'Turkey'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Eastern Mediterranean University,Faculty of Business and Economics"
    
    static_logo = "https://www.emu.edu.tr/static/images/logos/logo-name-en.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.emu.edu.tr/events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//div[contains(text(),'Load')]",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='listItemWrap']/a",next_page_xpath="//a[@class='nextPage']",get_next_month=True,click_next_month=False,wait_after_loading=False,run_script=False):
            for link in self.events_list(event_links_xpath="//a[@class='cardcontainer']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.emu.edu.tr/en/news/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@id='content']/h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//article[@class='posts']"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='eventfields']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='eventfields']"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
