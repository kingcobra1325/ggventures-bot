import scrapy, time
# from scrapy import Selector
from datetime import datetime

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller, EventBrite_API

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Usa0038Spider(scrapy.Spider):
    name = 'usa_0038'
    country = 'US'
    start_urls = ['https://carey.jhu.edu/contact']
    eventbrite_id = 30930596109

    def __init__(self):
        self.driver = Load_Driver()
        self.eventbrite_api = EventBrite_API()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None


    def parse(self, response):
        try:
            self.driver.get(response.url)
            # EVENTBRITE API - ORGANIZATION REQUEST
            raw_org = self.eventbrite_api.get_organizers(self.eventbrite_id)

            university_name = raw_org['name']
            if raw_org['logo']:
                logo = raw_org['logo']['url']
            else:
                logo = "https://brand.jhu.edu/assets/uploads/sites/5/2015/12/carey.logo_.small_.vertical.blue_.png"


            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='field__item']//article")))).text

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

            self.driver.get('https://carey.jhu.edu/news-events/events')

            number_of_months = 15
            #
            for scrape_month in range(number_of_months):

                try:
                    # time.sleep(10)

                    EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'event-title')]//a[contains(@rel,'bookmark')]")))

                    for i in EventLinks:

                        data = ItemLoader(item = GgventuresItem(), selector = i)

                        link = i.get_attribute('href')
                        self.getter.get(link)

                        # if 'isenberg.umass.edu/calendar/' in self.getter.current_url:

                        logger.info(f"Currently scraping --> {self.getter.current_url}")

                        # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail')]")))

                        # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail')]"))

                        data.add_value('university_name',university_name)
                        data.add_value('university_contact_info',university_contact_info)
                        data.add_value('logo',logo)
                        data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text)
                        # data.add_value('event_name', i.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
                        data.add_value('event_desc', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'text-with-summary')]"))).text)
                        # try:
                        #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'details')]/div[contains(@class,'wrapper')]").text)
                        # except NoSuchElementException as e:
                        #     logger.debug(f"Element cannot be located --> {e}")
                        data.add_value('event_date', self.getter.find_element(By.XPATH,"//h2[contains(text(),'Date')]/following-sibling::div").text)
                        data.add_value('event_time', self.getter.find_element(By.XPATH,"//h2[contains(text(),'Date')]/following-sibling::div").text)

                        # try:
                        #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text)
                        #     # data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                        # except NoSuchElementException as e:
                        #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        #     try:
                        #         data.add_value('event_date', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
                        #     except (TimeoutException,NoSuchElementException) as e:
                        #         logger.debug(f"Element cannot be located --> {e}")
                        #
                        #
                        # try:
                        #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text)
                        # except NoSuchElementException as e:
                        #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        #     try:
                        #         data.add_value('event_time', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
                        #     except (TimeoutException,NoSuchElementException) as e:
                        #         logger.debug(f"Element cannot be located --> {e}")

                        # data.add_value('event_link', link)
                        # try:
                            # event_phone = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_phone_number')]"))).text
                        #     event_phone =self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-tel')]").text
                        # except (TimeoutException,NoSuchElementException) as e:
                        #     logger.debug(f"Element cannot be located --> {e}")
                        #     event_phone = ''

                        # try:
                        #     # event_email = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_email')]"))).text
                        #     # event_email = self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-email')]").text
                        #     event_email = self.getter.find_element(By.XPATH,"//a[contains(@class,'event-email')]").get_attribute('textContent')
                        # except (TimeoutException,NoSuchElementException) as e:
                        #     logger.debug(f"Element cannot be located --> {e}")
                        #     event_email = ''
                        # data.add_value('startups_contact_info', event_email+'\n'+event_phone)
                        # data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,"//p[contains(text(),'Contact')]/parent::div").text.replace('CONTACT',''))

                        data.add_value('event_link', link)


                        yield data.load_item()

                except TimeoutException as e:
                    logger.debug(f"No available events for this month : {e} ---> Skipping...........")


                try:
                    # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'next-btn')]"))).click()
                    next_month = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'Go to next page')]"))).get_attribute('href')
                    self.driver.get(next_month)
                except TimeoutException as e:
                    logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
                    break


        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)

    def closed(self, reason):
        try:
            self.driver.quit()
            # self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
