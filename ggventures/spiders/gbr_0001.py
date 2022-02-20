import scrapy, time
# from scrapy import Selector
from datetime import datetime

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller, EventBrite_API

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Gbr0001Spider(scrapy.Spider):
    name = 'gbr_0001'
    # allowed_domains = ['https://aru.ac.uk/business-and-law']
    start_urls = ['https://aru.ac.uk/business-and-law/']
    country = 'United Kingdom'
    eventbrite_id = 1241978415

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.eventbrite_api = EventBrite_API()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            # EVENTBRITE API - ORGANIZATION REQUEST
            raw_org = self.eventbrite_api.get_organizers(self.eventbrite_id)

            university_name = raw_org['name']
            logo = raw_org['logo']['url']

            self.driver.get(response.url)

            # if not logo:
            #     logo = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@id,'footer-contact--phone-num')]/a")))).get_attribute('textContent')

            # EVENTBRITE API - EVENT LIST REQUEST
            raw_event = self.eventbrite_api.get_organizer_events(self.eventbrite_id)
            last_page = int(raw_event['pagination']['page_count'])
            prev_last_page = int(raw_event['pagination']['page_count']) - 1

            event_list = self.eventbrite_api.get_organizer_events(self.eventbrite_id,page=prev_last_page)['events'] + self.eventbrite_api.get_organizer_events(self.eventbrite_id,page=last_page)['events']

            for event in event_list:
                if datetime.strptime(event['start']['utc'].split('T')[0],'%Y-%m-%d') > datetime.utcnow():
                    data = ItemLoader(item = GgventuresItem(), selector = event)
                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    data.add_value('event_name', event['name']['text'])
                    data.add_value('event_desc', event['description']['text'])
                    data.add_value('event_date', f"Start Date: {event['start']['utc']} - End Date: {event['end']['utc']}")
                    data.add_value('event_link', event['url'])
                    # data.add_value('event_time', event_time[i])
                    yield data.load_item()

            # self.driver.get('https://calendar.uoregon.edu/calendar?event_types=22193')
            #
            # number_of_months = 12
            # #
            # for scrape_month in range(number_of_months):
            #
            #     try:
            #         # time.sleep(10)
            #
            #         EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//h3[contains(@class,'summary')]/a")))
            #
            #         for i in EventLinks:
            #
            #             data = ItemLoader(item = GgventuresItem(), selector = i)
            #
            #             link = i.get_attribute('href')
            #             self.getter.get(link)
            #
            #             # if 'isenberg.umass.edu/calendar/' in self.getter.current_url:
            #
            #             logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #             # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail')]")))
            #
            #             # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail')]"))
            #
            #             data.add_value('university_name',university_name)
            #             data.add_value('university_contact_info',university_contact_info)
            #             data.add_value('logo',logo)
            #             data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'summary')]"))).text)
            #             # data.add_value('event_name', i.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
            #             data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'description')]").text)
            #             # try:
            #             #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'details')]/div[contains(@class,'wrapper')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Element cannot be located --> {e}")
            #             data.add_value('event_date', self.getter.find_element(By.XPATH,"//p[contains(@class,'dateright')]").text)
            #             data.add_value('event_time', self.getter.find_element(By.XPATH,"//p[contains(@class,'dateright')]").text)
            #
            #             # try:
            #             #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text)
            #             #     # data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             #     try:
            #             #         data.add_value('event_date', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
            #             #     except (TimeoutException,NoSuchElementException) as e:
            #             #         logger.debug(f"Element cannot be located --> {e}")
            #             #
            #             #
            #             # try:
            #             #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             #     try:
            #             #         data.add_value('event_time', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
            #             #     except (TimeoutException,NoSuchElementException) as e:
            #             #         logger.debug(f"Element cannot be located --> {e}")
            #
            #             # data.add_value('event_link', link)
            #             # try:
            #                 # event_phone = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_phone_number')]"))).text
            #             #     event_phone =self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-tel')]").text
            #             # except (TimeoutException,NoSuchElementException) as e:
            #             #     logger.debug(f"Element cannot be located --> {e}")
            #             #     event_phone = ''
            #
            #             # try:
            #             #     # event_email = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_email')]"))).text
            #             #     # event_email = self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-email')]").text
            #             #     event_email = self.getter.find_element(By.XPATH,"//a[contains(@class,'event-email')]").get_attribute('textContent')
            #             # except (TimeoutException,NoSuchElementException) as e:
            #             #     logger.debug(f"Element cannot be located --> {e}")
            #             #     event_email = ''
            #             # data.add_value('startups_contact_info', event_email+'\n'+event_phone)
            #             # data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,"//p[contains(text(),'Contact')]/parent::div").text.replace('CONTACT',''))
            #
            #             data.add_value('event_link', link)
            #
            #
            #             yield data.load_item()
            #
            #     except TimeoutException as e:
            #         logger.debug(f"No available events for this month : {e} ---> Skipping...........")
            #
            #
            #     try:
            #         # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'next-btn')]"))).click()
            #         next_month = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@id,'next-number')]"))).get_attribute('href')
            #         self.driver.get(next_month)
            #     except TimeoutException as e:
            #         logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
            #         break



            # for i in EventLinks:
            #
            #     data = ItemLoader(item = GgventuresItem(), selector = i)
            #
            #     link = i.get_attribute('href')
            #     self.getter.get(link)
            #
            #     # if 'gatton.uky.edu/about-us' in self.getter.current_url:
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
            #     data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'masthead-title')]"))).text)
            #     # data.add_value('event_name', self.getter.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
            #     # data.add_value('event_desc', '\n'.join([x.text for x in WebDriverWait(self.getter,60).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@id,'event_detail_rightcol')]//div[contains(@class,'detail_block')]")))]))
            #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'row')]//div[contains(@class,'event-body')]").text)
            #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//dt[contains(text(),'When')]/following-sibling::dd").text)
            #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//dt[contains(text(),'When')]/following-sibling::dd").text)
            #     # try:
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #     # except NoSuchElementException as e:
            #     #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
            #     # data.add_value('event_link', link)
            #     # try:
            #     #     event_phone = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Phone')]/following-sibling::p"))).text
            #     # except TimeoutException as e:
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #     #     event_phone = ''
            #
            #     # try:
            #     #     event_email = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class,'contact')]"))).text
            #     # except TimeoutException as e:
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #     #     event_email = ''
            #     #
            #     #
            #     # data.add_value('startups_contact_info', event_email)
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
