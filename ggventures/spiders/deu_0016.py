from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Deu0016Spider(GGVenturesSpider):
    name = 'deu_0016'
    start_urls = ["https://www.rwth-aachen.de/cms/root/Die-RWTH/Kontakt-Anreise/~cxdn/Kontakt/lidx/1/"]
    country = 'Germany'
    # eventbrite_id = 30819498834

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "RWTH Aachen University"
    
    static_logo = "https://www.rwth-aachen.de/global/show_picture.asp?id=aaaaaaaaaaagazb"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.rwth-aachen.de/cms/root/Die-RWTH/Aktuell/~ulx/Veranstaltungen/lidx/1/"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.ClickMore(upcoming_events_xpath="//button[@class='filterable-list__load-more']")

            for link in self.multi_event_pages(num_of_pages=2,event_links_xpath="//div[@class='location']/a",next_page_xpath="//a[text()='Next Page']",get_next_month=True,click_next_month=False,wait_after_loading=False):
            # for link in self.events_list(event_links_xpath="//em[@class='filterable-list__list-item-meta']/../a"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring=["rwth-aachen.de","rwth-aachen.de/cms/root","https://www.rwth-aachen.de/go/id/"]):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()
                    
                    try:
                        item_data['event_name'] = self.scrape_xpath(xpath_list=["//div[@class='text']/h1"])
                        item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='text']","//div[contains(@class,'item-page')]/div[contains(@class,'row')]/div[contains(@class,'col')]"])
                    except NoSuchElementException:
                        continue
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='text']/h3","//div[contains(@class,'tile__content')]"],error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='text']/h3","//div[contains(@class,'tile__content')]"],error_when_none=False)
                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")
                    # item_data['event_time'] = self.get_datetime_attributes("//div[@class='aalto-article__info-text']/time")

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h6[contains(text(),'CONTACT')]/following-sibling::p"],error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
