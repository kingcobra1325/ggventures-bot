from pydoc import cli
from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0047Spider(GGVenturesSpider):
    name = 'fra_0047'
    start_urls = ["https://ils-assas-university.com/paris/"]
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Université Paris 2 - Panthéon-Assas,UFR de Sciences économiques et de gestion"
    
    static_logo = "https://www.u-paris2.fr/sites/default/files/paup-header.png"

    parse_code_link = "https://ils-assas-university.com/news-paris-campus/"

    university_contact_info_xpath = "//div[@class='iconbox_content_container ']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            # for link in self.events_list(event_links_xpath="//div[@class='media-actualite__contenu']/a"):
            for link in self.multi_event_pages(event_links_xpath="//a[@class='slide-image']",next_page_xpath="//a[contains(@class,'next_page')]",get_next_month=True):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://ils-assas-university.com/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1","//h3"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='entry-content']","//div[@class='nd-hide-900']/..","//div[@id='av_section_2']//div[contains(@class,'entry-content')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='entry-content']","//div[@class='nd-hide-900']/..","//div[@id='av_section_2']//div[contains(@class,'entry-content')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='entry-content']","//div[@class='nd-hide-900']/..","//div[@id='av_section_2']//div[contains(@class,'entry-content')]"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//span[@itemprop='organizer']/.."],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
