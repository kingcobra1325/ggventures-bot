from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Mex0002Spider(GGVenturesSpider):
    name = 'mex_0002'
    start_urls = ['https://www.itam.mx/']
    country = "Mexico"
    # eventbrite_id = 30819498834
    TRANSLATE = True

    handle_httpstatus_list = [402,403,404]

    static_name = "ITAM - Instituto Tecnológico Autónomo de México"
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Logo_del_ITAM.svg/1280px-Logo_del_ITAM.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://eventos.itam.mx/es/eventos"

    university_contact_info_xpath = "//h2[text()='Contacto']/.."
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'ullcalendar-container')]//a[not(text()='next') and not(text()='previous')]",checking_if_none=True)

            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//li[contains(@class,'overview-normal')]/a",next_page_xpath="//a[contains(@class,'loadMoreButton')]",get_next_month=False,click_next_month=True,wait_after_loading=True):
            for link in self.events_list(event_links_xpath="//div[contains(@class,'views-field-title')]/span[@class='field-content']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['eventos.itam.mx/es/evento']):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@id='titulo-evento']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='cuerpo-evento']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@id='fecha-evento']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@id='fecha-evento']"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[@id='mas-informacion']"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
