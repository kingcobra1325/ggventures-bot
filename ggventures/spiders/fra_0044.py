from pydoc import cli
from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Fra0044Spider(GGVenturesSpider):
    name = 'fra_0044'
    start_urls = ["https://iae.univ-lyon3.fr/visiting-faculty-1"]
    country = 'France'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "Université Lyon 3 - Jean Moulin,IAE de Lyon"
    
    static_logo = "https://iae.univ-lyon3.fr/uas/iae/LOGO/iae_2022_258x134px.png"

    parse_code_link = "https://iae.univ-lyon3.fr/accueil-en"

    university_contact_info_xpath = "//div[@class='ligne_4']//div[@class='paragraphe--0']"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            
            self.check_website_changed(upcoming_events_xpath="//li[text()='Aucun évenement']")
            
            # self.ClickMore(click_xpath="//strong[text()='Events']",run_script=True)

            # for link in self.events_list(event_links_xpath="//div[@class='media-actualite__contenu']/a"):
            # # for link in self.multi_event_pages(event_links_xpath="//div[@id='tab-future-events']//div[@class='col-12']/a",next_page_xpath="//i[@class='scpo-icon-arrow-right']",click_next_month=True):

            #     self.getter.get(link)

            #     if self.unique_event_checker(url_substring="https://seg.univ-lyon2.fr/presentation/actualites/evenements/"):

            #         logger.info(f"Currently scraping --> {self.getter.current_url}")

            #         item_data = self.item_data_empty.copy()

            #         item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent')
            #         item_data['event_link'] = link
            #         try:
            #             item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='contenu__interieur']").text
            #         except NoSuchElementException as e:
            #             logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[@class='nd-hide-900']/..").text

            #         try:
            #             item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[@class='actualite-dates']").text
            #             # item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[@class='inner-single-event-infos']//span[@class='value']").text
            #         except NoSuchElementException as e:
            #             logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[@class='date']").text
            #             # item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]").text

            #         try:
            #             item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//span[@itemprop='organizer']/..").text
            #             # item_data['startups_link'] = self.getter.find_element(By.XPATH,"//label[@class='bt-label']").text
            #         except NoSuchElementException as e:
            #             logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")

            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
