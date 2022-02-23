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

class Usa0073Spider(scrapy.Spider):
    name = 'usa_0073'
    # allowed_domains = ['https://www.fox.temple.edu/']
    start_urls = ['https://www.fox.temple.edu/contact-us/']
    country = 'US'
    eventbrite_id = 29609418151

    def __init__(self):
        self.driver = Load_Driver()
        self.eventbrite_api = EventBrite_API()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None


    def parse(self, response):
        try:
            # EVENTBRITE API - ORGANIZATION REQUEST
            raw_org = self.eventbrite_api.get_organizers(self.eventbrite_id)

            university_name = raw_org['name']
            if raw_org['logo']:
                logo = raw_org['logo']['url']
            else:
                logo = ''

            self.driver.get(response.url)

            # if not logo:
            #     logo = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'wp-block-column')]//div[contains(@class,'wp-block-column')]")))).text

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

            self.driver.get('https://www.fox.temple.edu/events/')

            EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'card-preview')]//a[contains(@class,'card-preview')]")))

            for i in EventLinks:

                data = ItemLoader(item = GgventuresItem(), selector = i)

                link = i.get_attribute('href')
                self.getter.get(link)

                # if 'gatton.uky.edu/about-us' in self.getter.current_url:

                logger.info(f"Currently scraping --> {self.getter.current_url}")

                # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]")))

                # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]"))

                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                data.add_value('logo',logo)
                data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).text)
                # data.add_value('event_name', self.getter.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
                # data.add_value('event_desc', '\n'.join([x.text for x in WebDriverWait(self.getter,60).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@id,'event_detail_rightcol')]//div[contains(@class,'detail_block')]")))]))
                data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'event--content')]").text)
                data.add_value('event_date', self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]/parent::span").text)
                data.add_value('event_time', self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::span").text)
                # try:
                #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                # except NoSuchElementException as e:
                #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                # data.add_value('event_link', link)
                # try:
                #     event_phone = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Phone')]/following-sibling::p"))).text
                # except TimeoutException as e:
                #     logger.debug(f"Element cannot be located --> {e}")
                #     event_phone = ''

                # try:
                #     event_email = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class,'contact')]"))).text
                # except TimeoutException as e:
                #     logger.debug(f"Element cannot be located --> {e}")
                #     event_email = ''
                #
                #
                # try:
                #     data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,"//section[contains(@class,'event-detail-contact-person')]").text)
                # except Exception as e:
                #     logger.debug(f"Error {e}: 'startups_contact_info' skipped")
                data.add_value('event_link', link)

                yield data.load_item()

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
