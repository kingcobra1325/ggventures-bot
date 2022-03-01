from binaries import logger
from spider_template import GGVenturesSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Chn0005Spider(GGVenturesSpider):
    name = 'chn_0005'
    start_urls = ['https://en.csu.edu.cn/index/Contact.htm']
    country = 'China'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = 'Central South University'
    static_logo = 'https://www.researchgate.net/publication/338246716/figure/fig2/AS:841997615112192@1577759283419/Logo-of-Central-South-University.jpg'

    # MAIN EVENTS LIST PAGE
    parse_code_link = 'https://en.csu.edu.cn/rili-events.jsp?urltype=tree.TreeTempUrl&wbtreeid=1084'

    university_contact_info_xpath = "//div[contains(@class,'Section1')]"
    contact_info_text = True
    # contact_info_textContent = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            # self.check_website_changed(upcoming_events_xpath="//p[contains(text(),'Sorry, no events for this category right now but check back later.')]")

            for link in self.multi_event_pages(num_of_pages=1,event_links_xpath="//div[contains(@class,'events-content')]//li/a",next_page_xpath="//a[contains(text(),'Next')]",get_next_month=True,click_next_month=False,wait_after_loading=False):
                # for link in self.events_list(event_links_xpath="//div[contains(@class,'news-content')]//li/a"):
                logger.debug(f"THIS IS THE LINK: {link}")

                if 'en.csu.edu.cn/rili-events-content.jsp' in link:
                    pass
                else:
                    continue

                self.getter.get(link)

                if self.unique_event_checker(url_substring='en.csu.edu.cn/rili-events-content.jsp'):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    try:
                        item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class,'vsbcontent_start')]"))).text
                    except (NoSuchElementException,TimeoutException) as e:
                        try:
                            logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                            item_data['event_name'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Topic')]/parent::p").text
                        except (NoSuchElementException,TimeoutException) as e:
                            try:
                                logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                                item_data['event_name'] = self.getter.find_element(By.XPATH,"//span[contains(text(),'Topic')]/parent::strong/parent::p").text
                            except (NoSuchElementException,TimeoutException) as e:
                                logger.debug(f"Error: {e}. XPath not located. Skipping link...")
                                continue




                    item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'content-content')]").text
                    # item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                    # item_data['event_time'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//p[contains(text(),'Time')]").text
                    except NoSuchElementException as e:
                        try:
                            logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                            item_data['event_date'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text
                            item_data['event_time'] = self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text
                        except NoSuchElementException as e:
                            try:
                                logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                                item_data['event_date'] = self.getter.find_element(By.XPATH,"//span[contains(text(),'Time')]/parent::strong/parent::p").text
                                item_data['event_time'] = self.getter.find_element(By.XPATH,"//span[contains(text(),'Time')]/parent::strong/parent::p").text
                            except NoSuchElementException as e:
                                logger.debug(f"Error: {e}. XPath not located. Skipping link...")
                                continue
                            # logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")


                    # item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//h3[text()='Contact']/..").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
