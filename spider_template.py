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


class GGVenturesSpider(scrapy.Spider):

    name : str = 'DefaultName'
    start_urls : list = 'DefaultUrl'
    country : str = 'DefaultCountry'
    eventbrite_id : int = 0

    USE_HANDLE_HTTPSTATUS_LIST = False

    if USE_HANDLE_HTTPSTATUS_LIST:
        handle_httpstatus_list = [403,404]

    eventbrite_id : int = 0

    university_contact_info : str = ''

    static_name : str = ''
    static_logo : str = ''

    parse_code_link : str = ''

    item_data_empty = {
                        'university_name' : '',
                        'university_contact_info' : '',
                        'logo' : '',
                        'event_name' : '',
                        'event_desc' : '',
                        'event_date' : '',
                        'event_link' : '',
                        'event_time' : '',
                        'startups_contact_info' : ''
                        }

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.eventbrite_api = EventBrite_API()
        self.start_time = round(time.time())
        self.scrape_time = None

    def unique_event_checker(self,url_substring=''):
        if url_substring:
            if url_substring in self.getter.current_url:
                return True
            elif 'www.eventbrite.com' in self.getter.current_url:
                logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. Skipping....")
                return False
            else:
                logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                logger.debug("Skipping............")
                return False
        else:
            logger.debug("No URL Substring. Proceed...")
            return True


    def load_item(self,item_data,item_selector):

        logger.info("INSIDE THE LOAD ITEM CODE")

        data = ItemLoader(item = GgventuresItem(), selector = item_selector)
        data.add_value('university_name', self.static_name)
        data.add_value('university_contact_info',self.university_contact_info)
        data.add_value('logo',self.static_logo)
        data.add_value('event_name', item_data['event_name'])
        data.add_value('event_desc', item_data['event_desc'])
        data.add_value('event_date', item_data['event_date'])
        data.add_value('event_link', item_data['event_link'])
        data.add_value('event_time', item_data['event_time'])
        data.add_value('startups_contact_info', item_data['startups_contact_info'])

        return data.load_item()

    def eventbrite_API_call(self,response):
        if self.eventbrite_id:
            # EVENTBRITE API - ORGANIZATION REQUEST
            logger.info("Eventbrite ID Detected. Processing...")
            raw_org = self.eventbrite_api.get_organizers(self.eventbrite_id)

            self.static_name = raw_org['name']

            if raw_org['logo']:
                logo = raw_org['logo']['url']
            else:
                logo = self.static_logo

            # EVENTBRITE API - EVENT LIST REQUEST
            raw_event = self.eventbrite_api.get_organizer_events(self.eventbrite_id)
            last_page = int(raw_event['pagination']['page_count'])
            prev_last_page = int(raw_event['pagination']['page_count']) - 1

            event_list = self.eventbrite_api.get_organizer_events(self.eventbrite_id,page=prev_last_page)['events'] + self.eventbrite_api.get_organizer_events(self.eventbrite_id,page=last_page)['events']

            for event in event_list:
                if datetime.strptime(event['start']['utc'].split('T')[0],'%Y-%m-%d') > datetime.utcnow():
                    data = ItemLoader(item = GgventuresItem(), selector = event)
                    data.add_value('university_name',self.static_name)
                    data.add_value('university_contact_info',self.university_contact_info)
                    data.add_value('logo',self.static_logo)
                    data.add_value('event_name', event['name']['text'])
                    data.add_value('event_desc', event['description']['text'])
                    data.add_value('event_date', f"Start Date: {event['start']['utc']} - End Date: {event['end']['utc']}")
                    data.add_value('event_link', event['url'])
                    # data.add_value('event_time', event_time[i])
                    yield data.load_item()
        else:
            logger.debug(f"No EventBrite ID Number...")

        logger.info("Proceed to Main Parse...")
        yield scrapy.Request(url=self.parse_code_link,callback=self.parse_code)

    def ClickMore(self,final_counter=10,start_counter=0):
        while True:
            try:
                LoadMore = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'more-results')]"))).click()
                logger.info("Load More Events....")
                time.sleep(10)
                counter+=1
                if counter >= final_counter:
                    logger.debug(f"Loaded all Events. Start Scraping......")
                    break
            except TimeoutException as e:
                logger.debug(f"No more Events to load --> {e}. Start Scraping......")
                break

    def get_university_contact_info(self):
        pass

    def parse_code(self,response):
        pass

    def parse(self, response):
        try:
            self.get_university_contact_info(response)
            logger.info("BEFORE EVENTBRITE CALL")
            yield scrapy.Request(url=response.url,callback=self.eventbrite_API_call)
            # self.parse_code()
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
