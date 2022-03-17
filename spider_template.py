import scrapy, time, traceback
# from scrapy import Selector
from datetime import datetime

from bot_email import missing_info_email, error_email, unique_event, website_changed

from binaries import Load_Driver, logger, WebScroller, EventBrite_API, GGV_SETTINGS

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from functools import wraps


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

    university_contact_info_xpath : str = ''
    contact_info_text = False
    contact_info_textContent = False
    contact_info_multispan = False

    item_data_empty = {
                        'university_name' : '',
                        'university_contact_info' : '',
                        'logo' : '',
                        'event_name' : '',
                        'event_desc' : '',
                        'event_date' : '',
                        'event_link' : '',
                        'event_time' : '',
                        'startups_contact_info' : '',
                        'startups_link' : '',
                        'startups_name' : ''
                        }

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.eventbrite_api = EventBrite_API()
        self.start_time = round(time.time())
        self.scrape_time = None

    def exception_handler(self,e):
        tb_log = traceback.format_exc()
        logger.exception(f"Experienced error on Spider: {self.name} --> {type(e).__name__}\n{e}. Sending Error Email Notification")
        err_message = f"{type(e).__name__}\nDRIVER URL: {self.driver.current_url}\nGETTER URL: {self.getter.current_url}\n{tb_log}"
        error_email(self.name,err_message)

    def unique_event_checker(self,url_substring=''):
        # CHECK IF NOT EMPTY
        if url_substring:
            # String - url_substring
            if isinstance(url_substring,str):
                if url_substring in self.getter.current_url:
                    return True
                elif 'www.eventbrite.com' in self.getter.current_url:
                    if not self.eventbrite_id:
                        logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. No EventBrite ID detected for Spider. Sending Emails...")
                        unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                        return False
                    else:
                        logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. Skipping....")
                        return False
                else:
                    logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                    unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                    logger.debug("Skipping............")
                    return False
            # List - url_substring
            if isinstance(url_substring,list):
                for url in url_substring:

                    if url in self.getter.current_url:
                        return True
                    elif 'www.eventbrite.com' in self.getter.current_url:
                        if not self.eventbrite_id:
                            logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. No EventBrite ID detected for Spider. Sending Emails...")
                            unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                            return False
                        else:
                            logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. Skipping....")
                            return False

                # No substring matching from list
                logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                logger.debug("Skipping............")
                return False

            else:
                logger.debug(f"URL Substring not a valid format --> {type(url_substring)}. Need to be a string or list. Proceed...")
        else:
            logger.debug("No URL Substring. Proceed...")
            return True


    def load_item(self,item_data,item_selector):

        data = ItemLoader(item = GgventuresItem(), selector = item_selector)
        data.add_value('university_name', self.static_name)
        data.add_value('university_contact_info',self.university_contact_info)
        data.add_value('logo',self.static_logo)
        data.add_value('event_name', item_data['event_name'])
        data.add_value('event_desc', item_data['event_desc'])
        data.add_value('event_date', item_data['event_date'])
        data.add_value('event_link', item_data['event_link'])
        data.add_value('event_time', item_data['event_time'])
        data.add_value('startups_link', item_data['startups_link'])
        data.add_value('startups_name', item_data['startups_name'])
        data.add_value('startups_contact_info', item_data['startups_contact_info'])

        logger.info(f"|LOADING| 'university_name' -> {self.static_name}")
        logger.info(f"|LOADING| 'university_contact_info' -> {self.university_contact_info}")
        logger.info(f"|LOADING| 'logo' -> {self.static_logo}")
        logger.info(f"|LOADING| 'event_name' -> {item_data['event_name']}")
        logger.info(f"|LOADING| 'event_desc' -> {item_data['event_desc']}")
        logger.info(f"|LOADING| 'event_date' -> {item_data['event_date']}")
        logger.info(f"|LOADING| 'event_link' -> {item_data['event_link']}")
        logger.info(f"|LOADING| 'event_time' -> {item_data['event_time']}")
        logger.info(f"|LOADING| 'startups_link' -> {item_data['startups_link']}")
        logger.info(f"|LOADING| 'startups_name' -> {item_data['startups_name']}")
        logger.info(f"|LOADING| 'startups_contact_info' -> {item_data['startups_contact_info']}")

        return data.load_item()

    def eventbrite_API_call(self,response):
        try:
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
        except Exception as e:
            self.exception_handler(e)

    def ClickMore(self,click_xpath='',counter=0,final_counter=10,run_script=False):
        while True:
            try:
                LoadMore = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
                if run_script:
                    self.driver.execute_script("arguments[0].click();", LoadMore)
                else:
                    LoadMore.click()
                logger.info("Load More Events....")
                time.sleep(10)
                counter+=1
                if counter >= final_counter:
                    logger.debug(f"Loaded all Events. Start Scraping......")
                    break
            except TimeoutException as e:
                logger.debug(f"No more Events to load --> {e}. Start Scraping......")
                break

    def get_university_contact_info(self,response):
        self.driver.get(response.url)

        if self.university_contact_info_xpath:
            if self.contact_info_text:
                self.university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.university_contact_info_xpath)))).text
            elif self.contact_info_textContent:
                self.university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.university_contact_info_xpath)))).get_attribute('textContent')
            elif self.contact_info_multispan:
                self.university_contact_info = '\n'.join([x.get_attribute('textContent') for x in WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH, self.university_contact_info_xpath)))])



    def parse_code(self,response):
        pass

    def parse(self, response):
        try:
            self.get_university_contact_info(response)
            yield scrapy.Request(url=response.url,callback=self.eventbrite_API_call)
        except Exception as e:
            self.exception_handler(e)

    def check_website_changed(self,upcoming_events_xpath='',empty_text=False,checking_if_none=False):
        try:
            no_events = WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located((By.XPATH,upcoming_events_xpath)))

            if checking_if_none:
                if no_events:
                    logger.debug('Changes to Events on current Spider. Sending emails....')
                    website_changed(self.name,self.static_name)
                else:
                    if empty_text:
                        logger.info("Empty Text check...")

                        logger.debug(f"no_events: {no_events}") if GGV_SETTINGS.DEBUG_LOGS else None
                        logger.debug(f"no_events type: {type(no_events)}") if GGV_SETTINGS.DEBUG_LOGS else None

                        no_events_text = ''.join([x.text for x in no_events])

                        logger.debug(f"no_events_text: '{no_events_text}'") if GGV_SETTINGS.DEBUG_LOGS else None

                        if no_events_text:
                            logger.debug('Text detected. Changes to Events on current Spider. Sending emails....')
                            website_changed(self.name,self.static_name)
                        else:
                            logger.debug('Empty Text. No changes to Events on current Spider. Skipping.....')
                    else:
                        logger.debug('No changes to Events on current Spider. Skipping.....')


            else:
                if not no_events:
                    logger.debug('Changes to Events on current Spider. Sending emails....')
                    website_changed(self.name,self.static_name)
                else:
                    if empty_text:
                        logger.info("Empty Text check...")

                        logger.debug(f"no_events: {no_events}") if GGV_SETTINGS.DEBUG_LOGS else None
                        logger.debug(f"no_events type: {type(no_events)}") if GGV_SETTINGS.DEBUG_LOGS else None

                        no_events_text = ''.join([x.text for x in no_events])

                        logger.debug(f"no_events_text: '{no_events_text}'") if GGV_SETTINGS.DEBUG_LOGS else None

                        if no_events_text:
                            logger.debug('Text detected. Changes to Events on current Spider. Sending emails....')
                            website_changed(self.name,self.static_name)
                        else:
                            logger.debug('Empty Text. No changes to Events on current Spider. Skipping.....')
                    else:
                        logger.debug('No changes to Events on current Spider. Skipping.....')
        except TimeoutException as e:
            if checking_if_none:
                logger.debug('No changes to Events on current Spider. Skipping.....')
            else:
                logger.debug(f"Upcoming Events XPATH cannot be located --> {e}")
                logger.debug('Changes to Events on current Spider. Sending emails....')
                website_changed(self.name,self.static_name)


    def events_list(self,event_links_xpath:str):

        web_elements_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,event_links_xpath)))
        logger.debug(f"Number of Event Links: {len(web_elements_list)}")
        return [x.get_attribute('href') for x in web_elements_list]


    def multi_event_pages(self,num_of_pages=6,event_links_xpath='',next_page_xpath='',get_next_month=False,click_next_month=False,wait_after_loading=False,no_next_page_xpath=''):

        event_links = []
        page_number = 0

        for scrape_page in range(num_of_pages):
            page_number = scrape_page + 2
            try:
                web_elements_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,event_links_xpath)))
                event_links.extend([x.get_attribute('href') for x in web_elements_list])

            except TimeoutException as e:
                logger.debug(f"No available events for this month : {e} ---> Skipping...........")

            if no_next_page_xpath:
                next_page_xpath = f"{no_next_page_xpath}[@rel='{page_number}']"

            try:
                if get_next_month:
                    next_month = self.driver.find_element(By.XPATH,next_page_xpath).get_attribute('href')
                    self.driver.get(next_month)
                if click_next_month:
                    WebDriverWait(self.driver,40).until(EC.element_to_be_clickable((By.XPATH,next_page_xpath))).click()
                # next_month = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'Go to the next page of the results')]"))).get_attribute('href')
                if wait_after_loading:
                    time.sleep(10)
            except (TimeoutException,NoSuchElementException) as e:
                logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
                break
            logger.debug(f"IN-PROGRESS: Pending Number of Event Links: {len(event_links)}")

        logger.debug(f"Number of Event Links: {len(event_links)}")
        return event_links

    def closed(self, reason):
        try:
            self.driver.quit()
            self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping closed due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            tb_log = traceback.format_exc()
            logger.exception(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            err_message = f"{type(e).__name__}\n{tb_log}\n{e}"
            error_email(self.name,err_message)
