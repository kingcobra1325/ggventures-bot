from distutils.log import error
from http.client import HTTPSConnection
from ssl import SSLCertVerificationError, SSLError
from numpy import maximum
import scrapy, time, traceback, gc
# from scrapy import Selector
from datetime import datetime

from bot_email import missing_info_email, error_email, unique_event, website_changed, file_event

from binaries import Load_Driver, WebScroller, EventBrite_API, GGV_SETTINGS, print_log
from lib.baselogger import initialize_logger

from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse

from ggventures.items import GgventuresItem

import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException, StaleElementReferenceException, NoSuchAttributeException, UnexpectedAlertPresentException, NoAlertPresentException,InvalidArgumentException
from googletrans import Translator

import re

from lib.error_dashboard import ErrorDashboard
from lib.decorators import decorate


logger = initialize_logger()

class GGVenturesSpider(scrapy.Spider):
    """
    Class where all of the spiders inherit to get all
    of the attributes and methods to be able to have a
    unified scraping process
    """

    name : str = 'DefaultName'
    start_urls : list = 'DefaultUrl'
    country : str = 'DefaultCountry'
    eventbrite_id : int = 0
    
    USE_FF_DRIVER = False

    USE_HANDLE_HTTPSTATUS_LIST = False

    TRANSLATE = True
    SRC_LANG = 'en'
    TL_LANG = 'en'
    TL_ITEM_EXCLUDE = [
                'university_name',
                'university_contact_info',
                'logo',
                # 'event_name',
                # 'event_desc',
                # 'event_date',
                'event_link',
                # 'event_time',
                'startups_contact_info',
                'startups_link',
                'startups_name',
                ]
    
    LIMIT_LINK_FETCHER : int = 0

    if USE_HANDLE_HTTPSTATUS_LIST:
        handle_httpstatus_list = [403,404]
    
    USE_MULTI_DRIVER = GGV_SETTINGS.MULTI_DRIVER

    class Func:
        print_log = print_log
        translator = Translator()
        def sleep(time_seconds=5):
            time.sleep(time_seconds)

    class Mth:
        By = By
        WebDriverWait = WebDriverWait
        Select = Select
        EC = EC
        WebScroller = WebScroller
        datetime = datetime
        website_changed = website_changed

    class Exc:
        NoSuchElementException = NoSuchElementException
        TimeoutException = TimeoutException
        StaleElementReferenceException = StaleElementReferenceException
        NoSuchAttributeException = NoSuchAttributeException

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

    PARSE_STATUS = 'success'

    def __init__(self):
        """
        Initialize the main/sub selenium drivers
        """
        self.driver = Load_Driver(self.USE_FF_DRIVER)
        if self.USE_MULTI_DRIVER:
            self.getter = Load_Driver(self.USE_FF_DRIVER)
        else:
            self.getter = self.driver
        self.eventbrite_api = EventBrite_API()
        self.start_time = round(time.time())
        self.scrape_time = None
    
    def request_api_call(self,url="",params={},payload="",method="GET"):
        """
        Method to do a request API call based on parameters
        """
        response = requests.request(method, url, params=params,data=payload).json()
        return response
            
        
    def convert_str_to_html(self,string):
        """
        Convert string into an html response that
        can be parsed via xpath/css etc.
        """
        response = HtmlResponse(url="converting string...", body=string, encoding='utf-8')
        return response

    def exception_handler(self,e):
        tb_log = traceback.format_exc()
        self.logger.exception(f"Experienced error on Spider: {self.name} --> {type(e).__name__}\n{e}. Sending Error Email Notification")
        err_message = f"{type(e).__name__}\nDRIVER URL: {self.driver.current_url}\nGETTER URL: {self.getter.current_url}\n{tb_log}"
        self.PARSE_STATUS = 'error'
        error_email(self.name,err_message)

    def translate_API_call(self,data):
        """
        Calls a translation api call to the data parameter
        """
        while True:
            try:
                result = self.Func.translator.translate(data)
                return result
            except Exception as e:
                self.logger.error(f"Translate API Error: {e}. Retrying...")

    def select_dropdown(self,xpath,value,wait_after_loading=False):
        dropdown = self.Mth.Select(self.driver.find_element(self.Mth.By.XPATH,xpath))
        dropdown.select_by_value(value)
        self.Func.sleep() if wait_after_loading else None

    def mat_select_dropdown(self,dropdown_xpath,option_xpath,wait_after_loading=False,run_script=False):

        dropdown = self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.element_to_be_clickable((self.Mth.By.XPATH, dropdown_xpath)))
        self.driver.execute_script("arguments[0].click();", dropdown) if run_script else dropdown.click()

        option = self.Mth.WebDriverWait(self.driver,20).until(self.Mth.EC.element_to_be_clickable((self.Mth.By.XPATH, option_xpath)))
        self.driver.execute_script("arguments[0].click();", option) if run_script else option.click()

        self.Func.sleep() if wait_after_loading else None



    def translate_text(self,raw_text=''):
        """
        Takes the parameter/parameters and run the API calls on
        all of the data and returns a translated dict/string
        """

        if isinstance(raw_text,dict):
            text_translated_dict = {}

            self.logger.debug(f"\nRAW TEXT: {raw_text}")
            self.logger.debug(f"TYPE: {type(raw_text)}")
            for k,v in raw_text.items():

                if k not in self.TL_ITEM_EXCLUDE:
                    result = self.translate_API_call(v)
                    text_translated_dict.update({k : result.text})

                    self.SRC_LANG = result.src
                    self.TL_LANG = result.dest

                    self.logger.debug(f"\nKEY |{k}|")
                    self.logger.debug(f"RAW LANG: {result.src}")
                    self.logger.debug(f"RAW TEXT: {result.origin}")
                    self.logger.debug(f"TRANSLATED LANG: {result.dest}")
                    self.logger.debug(f"TRANSLATED TEXT: {result.text}\n")

                    del result
                    gc.collect()

                else:
                    self.logger.debug(f"'{k}' included as Excluded from Translation. Loading Raw Data...")
                    text_translated_dict.update({k : v})

            self.logger.info(f"TRANSLATED TEXT DICT: {text_translated_dict}\n")

            del raw_text
            gc.collect()

            return text_translated_dict

        elif isinstance(raw_text,str):

            self.logger.debug(f"\nRAW TEXT: {raw_text}")
            self.logger.debug(f"TYPE: {type(raw_text)}")

            result = self.translate_API_call(raw_text)
            self.SRC_LANG = result.src
            self.TL_LANG = result.dest

            self.logger.debug(f"RAW LANG: {result.src}")
            self.logger.debug(f"RAW TEXT: {result.origin}")
            self.logger.debug(f"TRANSLATED LANG: {result.dest}")
            self.logger.debug(f"TRANSLATED TEXT: {result.text}\n")

            del raw_text
            gc.collect()

            return result

        else:
            self.logger.error(f"|raw_text| not a valid format --> {type(raw_text)}. Need to be a string or dict. Proceed...")


    def get_datetime_attributes(self,datetime_xpath,datetime_attribute='datetime',multi=True):
        """
        Get the datetime attribute of a web element
        """
        if multi:
            datetime_list = [x.get_attribute(datetime_attribute) for x in self.getter.find_elements(self.Mth.By.XPATH,datetime_xpath)]
            return '\n'.join(datetime_list)
        else:
            return self.getter.find_element(self.Mth.By.XPATH,datetime_xpath).get_attribute(datetime_attribute)
    
    def web_content_checker(self,check_link=''):
        ssl_verify_bool = True
        content_checker = ''
        
        list_contents = ['text/html','application/xml']

        while True:
            try:
                self.logger.debug('Checking URL Content...')
                if check_link:
                    content_checker = requests.head(check_link,verify=ssl_verify_bool).headers['Content-Type']
                    self.logger.debug(f'Currently checking : {check_link}')
                else:
                    content_checker = requests.head(self.getter.current_url,verify=ssl_verify_bool).headers['Content-Type']
                    self.logger.debug(f'Currently checking : {self.getter.current_url}')
                self.logger.debug(f'URL Content is {content_checker}')
                for content in list_contents:
                    self.logger.debug(F'Content Checker is [{content_checker}] while Content is [{content}]')
                    if content in content_checker:
                        return True
                return False
            except (requests.exceptions.SSLError):
                self.logger.debug('Web Content Checker went into exception')
                self.logger.debug('Switching SSL Verify to False')
                ssl_verify_bool = False

    def unique_event_checker(self,url_substring='',check_link=""):
        """
        Firstly checks if the url is a file or a html,
        Then checks the url of the getter driver if the
        parameter is a substring of the url
        """
        
        content_checker = self.web_content_checker(check_link)
        
        # CHECK IF PAGE NOT FOUND
        if self.getter.title.lower() not in ['page not found','404']:
            # CHECK IF NOT EMPTY
            if url_substring:
                # String - url_substring
                if isinstance(url_substring,str):
                    if not content_checker:
                            self.logger.debug(f"Link: {self.getter.current_url} is an File Event Link. Logging Events to Sheets ")
                            file_event(self,self.static_name,check_link,self.university_contact_info,self.static_logo)
                            return False
                    elif url_substring in self.getter.current_url:
                        return True
                    elif 'www.eventbrite.com' in self.getter.current_url:
                        if not self.eventbrite_id:
                            self.logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. No EventBrite ID detected for Spider. Sending Emails...")
                            unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                            return False
                        else:
                            self.logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. Skipping....")
                            return False
                    else:
                        self.logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                        unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                        self.logger.debug("Skipping............")
                        return False
                # List - url_substring
                if isinstance(url_substring,list):
                    for url in url_substring:
                        if not content_checker:
                            self.logger.debug(f"Link: {self.getter.current_url} is an File Event Link. Logging Events to Sheets ")
                            file_event(self,self.static_name,check_link,self.university_contact_info,self.static_logo)
                            return False
                        elif url in self.getter.current_url:
                            return True
                        elif 'www.eventbrite.com' in self.getter.current_url:
                            if not self.eventbrite_id:
                                self.logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. No EventBrite ID detected for Spider. Sending Emails...")
                                unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                                return False
                            else:
                                self.logger.debug(f"Link: {self.getter.current_url} is an Eventbrite Link. Skipping....")
                                return False

                    # No substring matching from list
                    self.logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                    unique_event(self,self.static_name,self.getter.current_url,self.university_contact_info,self.static_logo)
                    self.logger.debug("Skipping............")
                    return False

                else:
                    self.logger.debug(f"URL Substring not a valid format --> {type(url_substring)}. Need to be a string or list. Proceed...")
            else:
                self.logger.debug("No URL Substring. Proceed...")
                return True
        else:
            self.logger.debug("ERROR 404 FOUND... Skipping Spider")
            return False


    def get_links_from_source(self,link_base_list=['zoom']):
        """
        Gets all of the <a> web elements and filters
        for the links that meets the link base parameter
        """
        final_string = ''
        try:
            for link_base in link_base_list:
                self.logger.debug(f"LINK_BASE: {link_base}") if GGV_SETTINGS.DEBUG_LOGS else None
            get_all_links = [x.get_attribute('href') for x in self.getter.find_elements(By.TAG_NAME,'a') if isinstance(x.get_attribute('href'),str)]
            get_all_links = list(set(get_all_links))

            # FILTER LINK COUNT
            if self.LIMIT_LINK_FETCHER:
                self.logger.debug("LIMIT Fetched Links from Source...")
                self.logger.debug(f"Number of Links: {len(get_all_links)}")
                get_all_links = get_all_links[0:self.LIMIT_LINK_FETCHER]
                self.logger.debug(f"Number of Links After Filtering: {len(get_all_links)}")

            self.logger.debug(f"GET_ALL_LINKS:\n{get_all_links}")
            for link in get_all_links:
                if not link:
                    continue
                self.logger.debug(f"LINK: {link}")  if GGV_SETTINGS.DEBUG_LOGS else None
                if link_base in link:
                    self.logger.info(f"Link meets criteria as a startup link |{link_base}|. Adding...") if GGV_SETTINGS.DEBUG_LOGS else None
                    final_string = final_string + f"{link}\n"
                else:
                    self.logger.debug("Link doesn't meet the criteria. Skipping...") if GGV_SETTINGS.DEBUG_LOGS else None
            self.logger.debug(f"FINAL STRING: {final_string}")  if GGV_SETTINGS.DEBUG_LOGS else None
            del get_all_links
        except StaleElementReferenceException as e:
            self.logger.debug(f"ERROR: {e}. Skip fetching links...")  if GGV_SETTINGS.DEBUG_LOGS else None

        del link_base_list
        gc.collect()

        return final_string

    def get_emails_from_source(self,tag_list=['a'],attribute_name='href',driver_name='driver'):
        """
        Gets all of the emails from <a> web elements from the driver
        """
        all_emails = []
        get_all_emails = []
        final_all_emails = ''
        if driver_name.lower() == 'driver':
            email_driver = self.driver
        elif driver_name.lower() == 'getter':
            email_driver = self.getter
        else:
            self.logger.error(f"Invalid Driver Name |{driver_name}|. Returning None...")
            return None
        try:
            for tag in tag_list:
                get_all_emails = [x.get_attribute(attribute_name) for x in email_driver.find_elements(By.TAG_NAME,tag)][:GGV_SETTINGS.LIMIT_SCRAPED_EMAILS]
                get_all_emails = list(set(get_all_emails))
                self.logger.debug(f"TAG |{tag}| ATTRIBUTE |{attribute_name}| - Emails:\n{get_all_emails}")
                all_emails.extend(get_all_emails)
                self.logger.debug(f"FINAL ALL EMAILS TYPE {type(final_all_emails)} | ALL EMAILS TYPE {type(all_emails)}")
            all_emails = [str(x) for x in all_emails][:GGV_SETTINGS.LIMIT_SCRAPED_EMAILS]

             # FILTER LINK COUNT
            if self.LIMIT_LINK_FETCHER:
                self.logger.debug("LIMIT Fetched Emails from Source...")
                self.logger.debug(f"Number of Emails: {len(all_emails)}")
                all_emails = all_emails[0:self.LIMIT_LINK_FETCHER]
                self.logger.debug(f"Number of Emails After Filtering: {len(all_emails)}")

            final_all_emails = "\n".join(all_emails)
            self.logger.debug(f"ALL EMAILS FROM SOURCE:\n{final_all_emails}")
        except StaleElementReferenceException as e:
            self.logger.debug(f"ERROR: {e}. Skip fetching emails...")

        del all_emails
        del get_all_emails
        gc.collect()

        return final_all_emails

    def load_item(self,item_data,item_selector):
        """
        Loads the dict parameter onto the ItemLoader class
        and returns it
        """
        self.logger.debug(f"Translate |{self.TRANSLATE}|")
        if self.TRANSLATE:
            # Translate before Loading Items....
            item_data = self.translate_text(item_data)

        data = ItemLoader(item = GgventuresItem(), selector = item_selector)
        data.add_value('university_name', self.static_name)
        data.add_value('university_contact_info',self.university_contact_info[:5000])
        data.add_value('logo',self.static_logo)
        data.add_value('event_name', item_data['event_name'])
        data.add_value('event_desc', item_data['event_desc'][:5000])
        data.add_value('event_date', item_data['event_date'])
        data.add_value('event_link', item_data['event_link'])
        data.add_value('event_time', item_data['event_time'])
        data.add_value('startups_name', item_data['startups_name'])
        data.add_value('startups_contact_info', item_data['startups_contact_info'])
        if item_data['startups_link']:
            self.logger.debug(f"'startup_links' is loaded...") if GGV_SETTINGS.DEBUG_LOGS else None
            data.add_value('startups_link', item_data['startups_link'])
        else:
            self.logger.debug(f"'startup_links' is empty. Using get_links_from_source...") if GGV_SETTINGS.DEBUG_LOGS else None
            data.add_value('startups_link', self.get_links_from_source())

        self.logger.info(f"|LOADING| 'university_name' -> {self.static_name}")
        self.logger.info(f"|LOADING| 'university_contact_info' -> {self.university_contact_info}")
        self.logger.info(f"|LOADING| 'logo' -> {self.static_logo}")
        self.logger.info(f"|LOADING| 'event_name' -> {item_data['event_name']}")
        self.logger.info(f"|LOADING| 'event_desc' -> {item_data['event_desc']}")
        self.logger.info(f"|LOADING| 'event_date' -> {item_data['event_date']}")
        self.logger.info(f"|LOADING| 'event_link' -> {item_data['event_link']}")
        self.logger.info(f"|LOADING| 'event_time' -> {item_data['event_time']}")
        self.logger.info(f"|LOADING| 'startups_link' -> {item_data['startups_link']}")
        self.logger.info(f"|LOADING| 'startups_name' -> {item_data['startups_name']}")
        self.logger.info(f"|LOADING| 'startups_contact_info' -> {item_data['startups_contact_info']}")

        del item_data
        gc.collect()

        return data.load_item()

    def eventbrite_API_call(self,response):
        """
        The method that fetches all of the events from
        the Eventbrite API
        """
        try:
            if self.eventbrite_id:
                # EVENTBRITE API - ORGANIZATION REQUEST
                self.logger.info("Eventbrite ID Detected. Processing...")
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
                        data.add_value('event_time', f"Start Date: {event['start']['utc']} - End Date: {event['end']['utc']}")
                        data.add_value('event_link', event['url'])
                        # data.add_value('event_time', event_time[i])
                        yield data.load_item()

                        del data
                        gc.collect()
            else:
                self.logger.debug(f"No EventBrite ID Number...")

            self.logger.info("Proceed to Main Parse...")
            yield scrapy.Request(url=self.parse_code_link,callback=self.parse_code)
        except Exception as e:
            self.exception_handler(e)

    def ClickMore(self,click_xpath='',counter=0,final_counter=10,run_script=False):
        """
        Takes the xpath parameter and peform a browser click
        on it till the xpath cannot be located anymore
        """
        while True:
            try:
                LoadMore = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
                if run_script:
                    self.driver.execute_script("arguments[0].click();", LoadMore)
                else:
                    LoadMore.click()
                self.logger.info("Load More Events....")
                time.sleep(10)
                counter+=1
                if counter >= final_counter:
                    logger.debug(f"Loaded all Events. Start Scraping......")
                    break
            except TimeoutException as e:
                self.logger.debug(f"No more Events to load --> {e}. Start Scraping......")
                break

    @decorate.selenium_popup_handler_fn(exc=UnexpectedAlertPresentException)
    def get_university_contact_info(self,response):
        """
        Fetches the university contact info from the
        xpath attribute that will be called automatically
        """
        self.driver.get(response.url)
        
        if self.university_contact_info_xpath:
            self.logger.debug(f'Current URL for {self.country} is {self.getter.current_url}')
            if self.contact_info_text:
                self.university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.university_contact_info_xpath)))).text
            elif self.contact_info_textContent:
                self.university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.university_contact_info_xpath)))).get_attribute('textContent')
            elif self.contact_info_multispan:
                self.university_contact_info = '\n'.join([x.get_attribute('textContent') for x in WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH, self.university_contact_info_xpath)))])

            self.university_contact_info = f"{self.university_contact_info}\n{self.get_emails_from_source()}"
            

    def parse_code(self,response):
        """
        Template for spiders to write code into
        """
        pass

    def parse(self, response):
        """
        First method to be called automatically
        Runs the following methods by order:
            - get_university_contact_info
            - eventbrite_API_call
            - parse_code
        """
        try:
            self.get_university_contact_info(response)
            yield scrapy.Request(url=response.url,callback=self.eventbrite_API_call)
        except Exception as e:
            self.exception_handler(e)

    @decorate.conditional_function(GGV_SETTINGS.GET_IMAGES_DESCRIPTION)
    def desc_images(self,desc_xpath='',use_getter=True):
        try:
            if use_getter:
                temp_event_desc = self.getter.find_element(By.XPATH,desc_xpath)
            else:
                temp_event_desc = self.driver.find_element(By.XPATH,desc_xpath)
            list_images = "\n".join([str(x.get_attribute('src')) for x in temp_event_desc.find_elements(By.XPATH,'.//img')])
            return f"{temp_event_desc.get_attribute('textContent')} \nPicture Link(s):\n{list_images}"
        except NoSuchAttributeException as e:
            self.logger.debug(f"No image found on spider {self.name}... scraping text only...")
            return temp_event_desc.get_attribute('textContent')
    
    @decorate.conditional_function(GGV_SETTINGS.GET_IMAGES_DESCRIPTION)
    def desc_images_2(self,driver,xpath):
        try:
            temp_event_desc = driver.find_element(By.XPATH,xpath)
            list_images = "\n".join([str(x.get_attribute('src')) for x in temp_event_desc.find_elements(By.XPATH,'.//img')])
            return f"\nPictures Link(s):\n{list_images}"
        except NoSuchAttributeException as e:
            self.logger.debug(f"No image found on spider {self.name}... Skipping image description scraping.")
            return ""


    def alert_handler(self,alert_text='',alert_accept=True,alert_driver=None):
        try:
            self.Mth.WebDriverWait(alert_driver, 10).until(self.Mth.EC.alert_is_present(),alert_text)
            alert = alert_driver.switch_to.alert
            if alert_accept:
                alert.accept()
            else:
                alert.dismiss()
            self.logger.debug(f"Alert found and accepted... Proceeding to scrape spider {self.name}")
        except self.Exc.TimeoutException as e:
            self.logger.debug(f"No Alert found with text \"{alert_text}\" on spider {self.name}... Proceeding to scrape spider")


    def check_website_changed(self,upcoming_events_xpath='',empty_text=False,checking_if_none=False):
        """
        Method that checks if the xpath/element is located/changed
        from the website and sends an email notification if 
        changes are detected
        """
        try:
            no_events = WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located((By.XPATH,upcoming_events_xpath)))

            if checking_if_none:
                if no_events:
                    logger.debug('Changes to Events on current Spider. Sending emails....')
                    website_changed(self.name,self.static_name)
                    self.PARSE_STATUS = 'error'
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
                            self.PARSE_STATUS = 'error'
                        else:
                            logger.debug('Empty Text. No changes to Events on current Spider. Skipping.....')
                    else:
                        logger.debug('No changes to Events on current Spider. Skipping.....')


            else:
                if not no_events:
                    logger.debug('Changes to Events on current Spider. Sending emails....')
                    website_changed(self.name,self.static_name)
                    self.PARSE_STATUS = 'error'
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
                            self.PARSE_STATUS = 'error'
                        else:
                            logger.debug('Empty Text. No changes to Events on current Spider. Skipping.....')
                    else:
                        logger.debug('No changes to Events on current Spider. Skipping.....')
        except TimeoutException as e:
            if checking_if_none:
                self.logger.debug('No changes to Events on current Spider. Skipping.....')
            else:
                self.logger.debug(f"Upcoming Events XPATH cannot be located --> {e}")
                self.logger.debug('Changes to Events on current Spider. Sending emails....')
                website_changed(self.name,self.static_name)
                self.PARSE_STATUS = 'error'

    def scrape_xpath(self,driver='',xpath_list=[],method='text',error_when_none=True,enable_desc_image=False,wait_time=15):
        """
        Method to use to parse the data from a list of xpath
        and returns the data scraped and raises an error
        unless the parameter is disabled
        """
        image_desc = ""
        if not driver:
            driver = self.getter
        errors_dict = {}
        joined_xpath = " | ".join(xpath_list)
        if not method:
            try:
                parse_span = self.Mth.WebDriverWait(driver,5).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//span")))
                method = 'attr'
            except:
                method = 'text'
            
        try:
            if method.lower() == 'text':
                result = self.Mth.WebDriverWait(driver,wait_time).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,joined_xpath))).text
            else:
                result = self.Mth.WebDriverWait(driver,wait_time).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,joined_xpath))).get_attribute('textContent')
            if enable_desc_image:
                image_desc = self.desc_images_2(driver,joined_xpath)
            final_result = f"{result}\n{image_desc}"
            return final_result.strip()
        except self.Exc.TimeoutException as e:
            self.logger.debug(f"XPATH: {joined_xpath} cannot be scraped..")
            errors_dict.update({joined_xpath:f"|{type(e).__name__}\n{e}|"})
        if error_when_none:
            self.logger.error(f"No valid XPATH scraped...")
            xpath_errors = "\n".join([f"{k}{v}" for k,v in errors_dict.items()])
            error_message = f"No valid scrapable XPATH.\n{xpath_errors}"
            raise NoSuchElementException(error_message)
        else:
            self.logger.error(f"No valid XPATH scraped. Skipping...")
            return ""
    
    def switch_iframe(self,iframe_xpath="",error_when_none=True,iframe_driver=''):
        """
        With sites with iframe, switches to the iframe
        with the xpath continue scraping data within
        the iframe
        """
        if not iframe_driver:
            iframe_driver = self.getter
        try:
            self.Mth.WebDriverWait(iframe_driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,iframe_xpath)))
            self.Func.sleep(4)
        except self.Exc.TimeoutException as e:
            self.logger.debug(f"Iframe XPATH: {iframe_xpath} cannot be scraped..")
        if error_when_none:
            self.logger.error(f"No valid Iframe to switch...")
            raise NoSuchElementException()
        else:
            self.logger.error(f"No valid Iframe. Skipping...")
            return ""
        


    def events_list(self,event_links_xpath:str,return_elements=False,link_attribute='href',maximum_events=30):
        """
        Gets all of the event links from a list of elements based on the
        xpath provided on the parameter
        """
        try:
            web_elements_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,event_links_xpath)))
            self.logger.debug(f"Number of Event Links: {len(web_elements_list)}")
            if return_elements:
                return web_elements_list
            else:
                event_links = [x.get_attribute(link_attribute) for x in web_elements_list]
                # REMOVE EMPTY ELEMENTS
                cleaned_event_links = list(filter(None, event_links))
                # LIMIT EVENTS TO SCRAPE
                if not maximum_events:
                    del web_elements_list, event_links
                    gc.collect()
                    return cleaned_event_links
                else:
                    self.logger.debug(f"Maximum Events to scrape: {maximum_events}")
                    del web_elements_list, event_links
                    gc.collect()
                    if len(cleaned_event_links) >= maximum_events:
                        return cleaned_event_links[0:maximum_events]
                    else:
                        return cleaned_event_links
        except self.Exc.TimeoutException as e:
            self.logger.debug(f'No Events Found --> {e}. Skipping.....')
            return []
        
    def events_click_reveal(self,click_area_xpath=''):
        try:
            click_elements_list = WebDriverWait(self.driver,15).until(EC.presence_of_all_elements_located((By.XPATH,click_area_xpath)))
            for element in click_elements_list: 
                element.click()
        except self.Exc.TimeoutException as e:
            self.logger.debug(f'No clickable element Found --> {e}. Skipping.....')
            return []


    def get_no_page_xpath(self,next_page_xpath=''):
        return [x.get_attribute('href') for x in self.driver.find_elements(By.XPATH,next_page_xpath)]

    def find_href_button(self,href_button_xpath,base_site):
        button_links = [x.get_attribute('onclick') for x in self.driver.find_elements(By.XPATH,href_button_xpath)]
        new_list = []
        for btn in button_links:
            regexlink = re.search('href="\/\S+"',btn).group()
            regexnew= regexlink.replace('href=','').replace('\"','')
            new_list.append(f'{base_site}{regexnew}')
        return new_list
    
    def multi_event_dates(self,num_of_pages=6,date_xpath=""):
        date_list = []
        
        page_list = range(num_of_pages)
        
        for page in page_list:
            try:
                web_elements_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,date_xpath)))
                date_list.extend([x.get_attribute('textContent') for x in web_elements_list])
            except TimeoutException as e:
                self.logger.debug(f"No available events for this month : {e} ---> Skipping...........")
        return date_list


    def multi_event_pages(self,num_of_pages=6,event_links_xpath='',next_page_xpath='',get_next_month=False,click_next_month=False,wait_after_loading=False,click_month_list_xpath="",run_script=False\
        ,page_element='',current_page_class='',next_page_set_xpath='',href_button_xpath="",base_site="",elem_intercept_exc=False,maximum_events=30):
        """
        Gets all of the event links from a list of elements based on the
        xpath provided on the parameter and it will continue fetching
        the the links after switching to the next page via xpath
        """

        event_links = []
        page_links = []
        page_number = 0

        if click_month_list_xpath:
            pages_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,click_month_list_xpath)))
        else:
            pages_list = range(num_of_pages)

        if page_element and get_next_month:
            next_page_xpath = f"{next_page_xpath}{page_element}[not(contains(@class,'{current_page_class}'))]/a"
            page_links.extend(self.get_no_page_xpath(next_page_xpath))


        for scrape_page in pages_list:
            try:
                if href_button_xpath:
                    event_links.extend(self.find_href_button(href_button_xpath,base_site))
                else:
                    web_elements_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,event_links_xpath)))
                    event_links.extend([x.get_attribute('href') for x in web_elements_list])

            except TimeoutException as e:
                self.logger.debug(f"No available events for this month : {e} ---> Skipping...........")

            try:
                if click_month_list_xpath:
                    if run_script:
                        self.driver.execute_script("arguments[0].click();", scrape_page)
                    else:
                        scrape_page.click()
                else:
                    if page_element and get_next_month:
                        if len(page_links) == scrape_page and next_page_set_xpath:
                            self.driver.get(self.driver.find_element(By.XPATH,next_page_set_xpath).get_attribute('href'))
                            page_links.extend(self.get_no_page_xpath(next_page_xpath))
                        self.driver.get(page_links[scrape_page])
                    elif page_element and click_next_month:
                        page_number = scrape_page + 2
                        next_page_xpath = f"{page_element}[@{current_page_class}='{page_number}']"

                    if not page_element and get_next_month:
                        next_month = self.driver.find_element(By.XPATH,next_page_xpath).get_attribute('href')
                        try:
                            self.driver.get(next_month)
                        except InvalidArgumentException as e:
                            self.logger.debug(f"{e} --> No more pages to scrape")
                            break
                    if click_next_month:
                        next_page_btn = WebDriverWait(self.driver,40).until(EC.element_to_be_clickable((By.XPATH,next_page_xpath)))
                        if elem_intercept_exc:
                            try:
                                if run_script:
                                    self.driver.execute_script("arguments[0].click();", next_page_btn)
                                else:
                                    next_page_btn.click()
                            except ElementClickInterceptedException as e:
                                self.logger.debug(f"{e} --> No more pages to scrape")
                        else:
                            if run_script:
                                self.driver.execute_script("arguments[0].click();", next_page_btn)
                            else:
                                next_page_btn.click()
                    # next_month = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'Go to the next page of the results')]"))).get_attribute('href')
                if wait_after_loading:
                    time.sleep(10)
            except (TimeoutException,NoSuchElementException,IndexError) as e:
                self.logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
                break
            self.logger.debug(f"IN-PROGRESS: Pending Number of Event Links: {len(event_links)}")
            
        
        # REMOVE EMPTY ELEMENTS
        event_links = list(filter(None, event_links))
        self.logger.debug(f"Number of Event Links: {len(event_links)}")
        
        #LIMIT EVENTS TO SCRAPE
        if not maximum_events:
            return event_links
        else:
            self.logger.debug(f"Maximum Events to scrape: {maximum_events}")
            if len(event_links) >= maximum_events:
                return event_links[0:maximum_events]
            else:
                return event_links
            
        
    
    def handle_popup_alert(self,use_driver=True,action='cancel'):
        if use_driver:
            driver = self.driver
        else:
            driver = self.getter
        # Actions
        try:
            if action.lower() == 'cancel':
                driver.switch_to.alert().dismiss()
            elif action.lower() == 'ok':
                driver.switch_to.alert().accept()
                # driver.switchTo().alert().accept()
            else:
                raise Exception(f"Invalid pop-up action - {action}...")
        except NoAlertPresentException as e:
            self.logger.debug(f"|{e}| No Alert present...")


    def closed(self, reason):
        """
        The method called after the spider is closed.
        Closes all of the WebDrivers
        """
        try:
            error_dashboard = ErrorDashboard()
            error_dashboard.process_spider_status(self.name,self.PARSE_STATUS)
            del error_dashboard
            self.driver.quit()
            if self.USE_MULTI_DRIVER:
                self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            gc.collect()
            self.logger.debug(f"Spider: {self.name} scraping closed due to --> {reason}")
            self.logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            tb_log = traceback.format_exc()
            self.logger.exception(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            err_message = f"{type(e).__name__}\n{tb_log}\n{e}"
            error_email(self.name,err_message)
