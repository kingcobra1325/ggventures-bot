import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Usa0117Spider(scrapy.Spider):
    name = 'usa_0117'
    # allowed_domains = ['https://business.louisville.edu/academics-programs/graduate-programs/']
    start_urls = ['https://business.louisville.edu/academics-programs/graduate-programs/']
    country = 'US'

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:

            self.driver.get(response.url)

            logo = 'https://media.bizj.us/view/img/10893599/uofl-logo.png'

            university_name = 'University of Louisville, College of Business and Public Administration'

            university_contact_info = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//address/following-sibling::a"))).get_attribute('textContent')

            self.driver.get('https://events.louisville.edu/calendar')

            # WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Classic Table Calendar View')]")))
            #
            # #
            number_of_months = 15
            #
            for scrape_month in range(number_of_months):

                try:
                    time.sleep(10)

                    EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//h3[contains(@class,'summary')]/a")))

                    for i in EventLinks:

                        data = ItemLoader(item = GgventuresItem(), selector = i)

                        link = i.get_attribute('href')
                        self.getter.get(link)

                        # if 'saunders.rit.edu/events' in self.getter.current_url:

                        logger.info(f"Currently scraping --> {self.getter.current_url}")

                        # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail')]")))

                        # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail')]"))

                        data.add_value('university_name',university_name)
                        data.add_value('university_contact_info',university_contact_info)
                        data.add_value('logo',logo)
                        data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'summary')]"))).text)
                        # data.add_value('event_name', i.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
                        data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'description')]").text)
                        data.add_value('event_date', self.getter.find_element(By.XPATH,"//p[contains(@class,'dateright')]").text)
                        data.add_value('event_time', self.getter.find_element(By.XPATH,"//p[contains(@class,'dateright')]").text)
                        # try:
                        #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                        #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                        # except NoSuchElementException as e:
                        #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                        #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                        # data.add_value('event_link', link)
                        try:
                            # event_phone = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_phone_number')]"))).text
                            event_phone =self.getter.find_element(By.XPATH,"//dd[contains(@class,'contact_phone_number')]").text
                        except (TimeoutException,NoSuchElementException) as e:
                            logger.debug(f"Element cannot be located --> {e}")
                            event_phone = ''

                        try:
                            # event_email = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_email')]"))).text
                            event_email = self.getter.find_element(By.XPATH,"//dd[contains(@class,'contact_email')]").text
                        except (TimeoutException,NoSuchElementException) as e:
                            logger.debug(f"Element cannot be located --> {e}")
                            event_email = ''
                        data.add_value('startups_contact_info', event_email+'\n'+event_phone)

                        data.add_value('event_link', link)


                        yield data.load_item()

                except TimeoutException as e:
                    logger.debug(f"No available events for this month : {e} ---> Skipping...........")


                # try:
                #     WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'Next Page')]"))).click()
                # except TimeoutException as e:
                #     logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
                #     break
                # self.driver.find_element(By.XPATH,"//a[contains(@title,'Next Page')]").click()
                next_month = self.driver.find_element(By.XPATH,"//a[contains(@id,'next-number')]").get_attribute('href')
                self.driver.get(next_month)
                # time.sleep(10)

            # self.driver.switch_to.frame(WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@title,'List Calendar View')]"))))

            # WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Events')]")))

            # ClickMore = self.driver.find_elements(By.XPATH,"//div[contains(@id,'day')]")
            #
            # for Click in ClickMore:
            #     Click.click()
            #     time.sleep(5)
            #
            # time.sleep(10)



            # EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'events-link')]")))
            #
            # for i in EventLinks:
            #
            #     data = ItemLoader(item = GgventuresItem(), selector = i)
            #
            #     link = i.get_attribute('href')
            #     self.getter.get(link)
            #
            #     # if 'groups.stanford.edu' in self.getter.current_url:
            #
            #     logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #     # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]")))
            #
            #     # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]"))
            #
            #     data.add_value('university_name',university_name)
            #     data.add_value('university_contact_info',university_contact_info)
            #     data.add_value('logo',logo)
            #     data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'updates-title')]"))).text)
            #     # data.add_value('event_name', self.getter.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
            #     # data.add_value('event_desc', '\n'.join([x.text for x in WebDriverWait(self.getter,60).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@id,'event_detail_rightcol')]//div[contains(@class,'detail_block')]")))]))
            #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'column three-quarter')]").text)
            #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//time[contains(@class,'tBottom')]").text)
            #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//time[contains(@class,'tBottom')]").text)
            #     # try:
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #     # except NoSuchElementException as e:
            #     #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
            #     # data.add_value('event_link', link)
            #     # try:
            #     #     event_phone = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Phone')]/following-sibling::p"))).text
            #     # except TimeoutException as e:
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #     #     event_phone = ''
            #
            #     try:
            #         event_email = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class,'contact')]"))).text
            #     except TimeoutException as e:
            #         logger.debug(f"Element cannot be located --> {e}")
            #         event_email = ''
            #
            #
            #     data.add_value('startups_contact_info', event_email)
            #     data.add_value('event_link', link)
            #
            #     yield data.load_item()

                # self.getter.switch_to.default_content()
                # else:
                #     logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                #     unique_event(self.name,university_name,self.getter.current_url)
                #     logger.debug("Skipping............")

                # WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@rel,'next')]"))).click()
                # time.sleep(10)

        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
    def closed(self, reason):
        try:
            self.driver.quit()
            self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
