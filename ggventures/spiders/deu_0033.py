from spider_template import GGVenturesSpider


class Deu0033Spider(GGVenturesSpider):
    name = 'deu_0033'
    start_urls = ["https://www.uni-wh.de/en/uwh-international/university/faculty-of-management-economics-and-society/deans-office-and-bodies/"]
    country = 'Germany'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Universität Witten-Herdecke,Faculty of Management and Economics"
    
    static_logo = "https://d30mzt1bxg5llt.cloudfront.net/public/uploads/images/_signatoryLogo/Uni-Logo.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uni-wh.de/suche/?tab=event&c1=off"

    university_contact_info_xpath = "//div[@id='c4271']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'c-events')]",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//h4/a",next_page_xpath="//span[text()='Weiter']/..",get_next_month=True,click_next_month=False,wait_after_loading=False):
            for link in self.events_list(event_links_xpath="//a[@class='detail-link']"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.uni-wh.de/detailseiten/news/"]):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='desktop-headline']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='content-standard-left']"])
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Termin')]/following-sibling::div","//div[contains(@class,'inner-box information')]","//div[contains(@class,'odd-even-table')]//div[contains(@class,'content-tabelle-row')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Termin')]/following-sibling::div","//div[contains(@class,'inner-box information')]","//div[contains(@class,'odd-even-table')]//div[contains(@class,'content-tabelle-row')]"],method='attr')
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(text(),'Kontakt')]/following-sibling::div"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    


                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
