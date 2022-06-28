from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Mex0003Spider(GGVenturesSpider):
    name = 'mex_0003'
    start_urls = ['https://tec.mx/es/contactanos']
    country = "Mexico"
    # eventbrite_id = 30819498834
    TRANSLATE = True

    # handle_httpstatus_list = [403,404]

    static_name = "ITESM - Campus Estado de México"
    static_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIpzUZxQQKmLoIdbmok1AeBlQUj0M-nJl17g&usqp=CAU"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://conecta.tec.mx/es/noticias/eventos"

    university_contact_info_xpath = "//div[@class='columnas_texto columnas_texto--  ']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'ullcalendar-container')]//a[not(text()='next') and not(text()='previous')]",checking_if_none=True)

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[contains(@class,'overview-normal')]/a",next_page_xpath="//a[contains(@class,'loadMoreButton')]",get_next_month=False,click_next_month=True,wait_after_loading=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'views-field-title')]/span[@class='field-content']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['tec.mx/es/noticias/eventos']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='evento-crp']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='evento-hdr']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='evento-hdr']"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@class='evento-cont']"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
