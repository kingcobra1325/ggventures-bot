
from spider_template import GGVenturesSpider


class Zwe0001Spider(GGVenturesSpider):
    name = 'zwe_0001'
    start_urls = ['https://nbs.nust.edu.pk/contact/']
    country = "Zimbabwe"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "National University of Science and Technology Business School"
    static_logo = "https://www.result.pk/_images/articles/images/2019-04/3405_1_24605.jpg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://nbs.nust.edu.pk/events/"

    university_contact_info_xpath = "//body"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'all_posts_event')]//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//a[@id='btnLoadMore']",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[contains(@class,'fc-view-month')]//a",next_page_xpath="//span[contains(@class,'ui-corner-right')]",click_next_month=True,run_script=True,wait_after_loading=True):
            # for link in self.events_list(event_links_xpath="//h6/a"):
            #     self.getter.get(f"{link}")
            #     if self.unique_event_checker(url_substring=['qau.edu.ye/en/news']):

            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

            #         item_data = self.item_data_empty.copy()

            #         # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

            #         item_data['event_name'] = self.scrape_xpath(xpath_list=["//h2"])
            #         item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='post__content']"])
            #         item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='post__content']"])
            #         item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='post__content']"])

            #         # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''
            #         item_data['event_link'] = link

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
