from spider_template import GGVenturesSpider


class Ven0002Spider(GGVenturesSpider):
    name = 'ven_0002'
    start_urls = ["https://urfu.ru/ru/contacts/"]
    country = 'Venezuela'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universidad Central de Venezuela,Facultad de Ciencias Económicas y Sociales"
    
    static_logo = "http://www.ucv.ve/fileadmin/templates/core/img/ucv.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://urfu.ru/ru/events/s"

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
            
            self.ClickMore(click_xpath="//a[text()='Больше событий']",run_script=True)
            
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[starts-with(@class,'event-calendar__day-wrap')]//a",next_page_xpath="//span[starts-with(@class,'icon-arrow-calendar')][2]",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//p[@class='title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://urfu.ru/ru/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='article']/h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='article']"],method='attr',enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[@class='date']"],method='attr')
                    # item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='event-info']"],method='attr')

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
