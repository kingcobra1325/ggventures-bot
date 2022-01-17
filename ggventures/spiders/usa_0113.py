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


class Usa0113Spider(scrapy.Spider):
    name = 'usa_0113'
    # allowed_domains = ['https://www.hartford.edu/academics/schools-colleges/barney/default.aspx']
    start_urls = ['https://www.hartford.edu/contact.aspx']
    country = 'US'

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:

            self.driver.get(response.url)

            logo = 'https://media-exp1.licdn.com/dms/image/C4D0BAQF3Lr0HqsVNyQ/company-logo_200_200/0/1599249881343?e=2159024400&v=beta&t=ALfgFW3yRjbGP6_v8gMNsswaq5X_9CPZW2mYprWRLw4'

            university_name = 'University of Hartford, The Barney School of Business'

            university_contact_info = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,' Content Section 1 ')]"))).text

            self.driver.get('https://www.hartford.edu/calendar/default.aspx')

            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'List Calendar View')]")))

            number_of_months = 9
            #
            for scrape_month in range(number_of_months):

                try:
                    time.sleep(10)

                    EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'twDescription')]/a")))

                    for i in EventLinks:

                        data = ItemLoader(item = GgventuresItem(), selector = i)

                        link = i.get_attribute('href')
                        self.getter.get(link)

                        # if 'saunders.rit.edu/events' in self.getter.current_url:

                        logger.info(f"Currently scraping --> {self.getter.current_url}")

                        # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]")))

                        # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]"))

                        data.add_value('university_name',university_name)
                        data.add_value('university_contact_info',university_contact_info)
                        data.add_value('logo',logo)
                        data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'twEDDescription')]"))).text)
                        # data.add_value('event_name', i.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
                        data.add_value('event_desc', self.getter.find_element(By.XPATH,"//table[contains(@class,'twEDContent')]").text)
                        data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'twEDStartEndRange')]").text)
                        data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'twEDStartEndRange')]").text)
                        # try:
                        #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                        #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                        # except NoSuchElementException as e:
                        #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                        #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                        # data.add_value('event_link', link)
                        data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,'//dt[contains(@class,//dt[contains(@class,"event_contact_email")]/following-sibling::dd').text)

                        data.add_value('event_link', link)


                        yield data.load_item()

                except TimeoutException as e:
                    logger.debug(f"No available events for this month : {e} ---> Skipping...........")

                # WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@aria-label,'Next Page')]"))).click()
                self.driver.find_element(By.XPATH,"//a[contains(@aria-label,'Next Page')]").click()
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



            # EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'emu-card_title-link')]")))
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
            #     try:
            #         event_phone = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Phone')]/following-sibling::p"))).text
            #     except TimeoutException as e:
            #         logger.debug(f"Element cannot be located --> {e}")
            #         event_phone = ''
            #
            #     try:
            #         event_email = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Email')]/following-sibling::p"))).text
            #     except TimeoutException as e:
            #         logger.debug(f"Element cannot be located --> {e}")
            #         event_email = ''
            #
            #     data.add_value('university_name',university_name)
            #     data.add_value('university_contact_info',university_contact_info+"\n"+event_phone+"\n"+event_email)
            #     data.add_value('logo',logo)
            #     data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'card_title')]"))).text)
            #     # data.add_value('event_name', self.getter.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
            #     # data.add_value('event_desc', '\n'.join([x.text for x in WebDriverWait(self.getter,60).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@id,'event_detail_rightcol')]//div[contains(@class,'detail_block')]")))]))
            #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'em-about_description')]").text)
            #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//p[contains(@class,'em-date')]").text)
            #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//p[contains(@class,'em-date')]").text)
            #     # try:
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #     # except NoSuchElementException as e:
            #     #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
            #     # data.add_value('event_link', link)
            #     data.add_value('event_link', link)
            #
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
