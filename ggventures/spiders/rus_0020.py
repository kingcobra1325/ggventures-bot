from spider_template import GGVenturesSpider


class Rus0020Spider(GGVenturesSpider):
    name = "rus_0020"
    start_urls = ["https://www.hse.ru/en/"]
    country = "Russia"
    # eventbrite_id = 8447939505
# 
    # handle_httpstatus_list = [301,302,403,404]

    static_name = "HSE University"
    
    static_logo = "https://keystoneacademic-res.cloudinary.com/image/upload/element/15/157257_HSE_University_blue1.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.hse.ru/en/news/announcements/"

    university_contact_info_xpath = "//h2[text()='Contacts']/../.."
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
            for link in self.events_list(event_links_xpath="//div[contains(@class,'b-events__body_title')]//a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["hse.ru"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//*[@class='post-title' or @class='post_single' or contains(@class,'promo-title')]"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='post__text' or @class='post__text' or @class='content__inner']"],enable_desc_image=True,error_when_none=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'g-day__title') or @class='post-meta__date' or @class='fa-card__category']","//span[contains(text(),'Date')]/../..","//h2[@class='promo-subtitle']","//li[@class='icon ion-calendar']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'g-day__title') or @class='post-meta__date' or @class='fa-card__category']","//span[contains(text(),'Date')]/../.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='article-coordination-info']"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
