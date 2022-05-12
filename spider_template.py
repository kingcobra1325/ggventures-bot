import scrapy, time, traceback, os, sys
# from scrapy import Selector
from datetime import datetime

from bot_email import missing_info_email, error_email, unique_event, website_changed

from binaries import Load_Driver, logger, WebScroller, EventBrite_API, GGV_SETTINGS, print_log

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, NoSuchAttributeException

from googletrans import Translator

import re

class GGVenturesSpider(scrapy.Spider):

    name : str = 'DefaultName'
    start_urls : list = 'DefaultUrl'
    country : str = 'DefaultCountry'
    eventbrite_id : int = 0

    USE_HANDLE_HTTPSTATUS_LIST = False

    TRANSLATE = False
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


    def __init__(self):
        self.driver = Load_Driver()
        if self.USE_MULTI_DRIVER:
            self.getter = Load_Driver()
        else:
            self.getter = self.driver
        self.eventbrite_api = EventBrite_API()
        self.start_time = round(time.time())
        self.scrape_time = None

    def exception_handler(self,e):
        tb_log = traceback.format_exc()
        logger.exception(f"Experienced error on Spider: {self.name} --> {type(e).__name__}\n{e}. Sending Error Email Notification")
        err_message = f"{type(e).__name__}\nDRIVER URL: {self.driver.current_url}\nGETTER URL: {self.getter.current_url}\n{tb_log}"
        error_email(self.name,err_message)

    def translate_API_call(self,data):
        while True:
            try:
                result = self.Func.translator.translate(data)
                return result
            except Exception as e:
                self.Func.print_log(f"Translate API Error: {e}. Retrying...",'error')

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

        if isinstance(raw_text,dict):
            text_translated_dict = {}

            self.Func.print_log(f"\nRAW TEXT: {raw_text}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            self.Func.print_log(f"TYPE: {type(raw_text)}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            for k,v in raw_text.items():

                if k not in self.TL_ITEM_EXCLUDE:
                    result = self.translate_API_call(v)
                    text_translated_dict.update({k : result.text})

                    self.SRC_LANG = result.src
                    self.TL_LANG = result.dest

                    self.Func.print_log(f"\nKEY |{k}|",'debug')
                    self.Func.print_log(f"RAW LANG: {result.src}",'debug',GGV_SETTINGS.DEBUG_LOGS)
                    self.Func.print_log(f"RAW TEXT: {result.origin}",'debug',GGV_SETTINGS.DEBUG_LOGS)
                    self.Func.print_log(f"TRANSLATED LANG: {result.dest}",'debug',GGV_SETTINGS.DEBUG_LOGS)
                    self.Func.print_log(f"TRANSLATED TEXT: {result.text}\n",'debug',GGV_SETTINGS.DEBUG_LOGS)

                else:
                    self.Func.print_log(f"'{k}' included as Excluded from Translation. Loading Raw Data...",'debug',GGV_SETTINGS.DEBUG_LOGS)
                    text_translated_dict.update({k : v})

            self.Func.print_log(f"TRANSLATED TEXT DICT: {text_translated_dict}\n",'info')

            return text_translated_dict

        elif isinstance(raw_text,str):

            self.Func.print_log(f"\nRAW TEXT: {raw_text}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            self.Func.print_log(f"TYPE: {type(raw_text)}",'debug',GGV_SETTINGS.DEBUG_LOGS)

            result = self.translate_API_call(raw_text)
            self.SRC_LANG = result.src
            self.TL_LANG = result.dest

            self.Func.print_log(f"RAW LANG: {result.src}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            self.Func.print_log(f"RAW TEXT: {result.origin}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            self.Func.print_log(f"TRANSLATED LANG: {result.dest}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            self.Func.print_log(f"TRANSLATED TEXT: {result.text}\n",'debug',GGV_SETTINGS.DEBUG_LOGS)

            return result

        else:
            self.Func.print_log(f"|raw_text| not a valid format --> {type(raw_text)}. Need to be a string or dict. Proceed...","error")


    def get_datetime_attributes(self,datetime_xpath,datetime_attribute='datetime'):
        datetime_list = [x.get_attribute(datetime_attribute) for x in self.getter.find_elements(self.Mth.By.XPATH,datetime_xpath)]
        return '\n'.join(datetime_list)

    def unique_event_checker(self,url_substring=''):
        # CHECK IF PAGE NOT FOUND
        if self.getter.title.lower() not in ['page not found','404']:
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
        else:
            logger.debug("ERROR 404 FOUND... Skipping Spider")
            return False


    def get_links_from_source(self,link_base_list=['zoom']):
        final_string = ''
        try:
            for link_base in link_base_list:
                logger.debug(f"LINK_BASE: {link_base}") if GGV_SETTINGS.DEBUG_LOGS else None
            get_all_links = [x.get_attribute('href') for x in self.getter.find_elements(By.TAG_NAME,'a')]
            get_all_links = list(set(get_all_links))
            self.Func.print_log(f"GET_ALL_LINKS:\n{get_all_links}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            for link in get_all_links:
                if not link:
                    continue
                logger.debug(f"LINK: {link}")  if GGV_SETTINGS.DEBUG_LOGS else None
                if link_base in link:
                    logger.info(f"Link meets criteria as a startup link |{link_base}|. Adding...") if GGV_SETTINGS.DEBUG_LOGS else None
                    final_string = final_string + f"{link}\n"
                else:
                    logger.debug("Link doesn't meet the criteria. Skipping...") if GGV_SETTINGS.DEBUG_LOGS else None
            logger.debug(f"FINAL STRING: {final_string}")  if GGV_SETTINGS.DEBUG_LOGS else None
        except StaleElementReferenceException as e:
            logger.debug(f"ERROR: {e}. Skip fetching links...")  if GGV_SETTINGS.DEBUG_LOGS else None
        return final_string

    def get_emails_from_source(self,tag_list=['a'],attribute_name='href',driver_name='driver'):
        all_emails = []
        final_all_emails = []
        if driver_name.lower() == 'driver':
            email_driver = self.driver
        elif driver_name.lower() == 'getter':
            email_driver = self.getter
        else:
            self.Func.print_log(f"Invalid Driver Name |{driver_name}|. Returning None...",'error')
            return None
        try:
            for tag in tag_list:
                get_all_emails = [x.get_attribute(attribute_name) for x in email_driver.find_elements(By.TAG_NAME,tag)]
                get_all_emails = list(set(get_all_emails))
                self.Func.print_log(f"TAG |{tag}| ATTRIBUTE |{attribute_name}| - Emails:\n{get_all_emails}",'debug',GGV_SETTINGS.DEBUG_LOGS)
                all_emails.extend(get_all_emails)
                self.Func.print_log(f"FINAL ALL EMAILS TYPE {type(final_all_emails)} | ALL EMAILS TYPE {type(all_emails)}",'debug',GGV_SETTINGS.DEBUG_LOGS)
            all_emails = [str(x) for x in all_emails]
            final_all_emails = "\n".join(all_emails)
            self.Func.print_log(f"ALL EMAILS FROM SOURCE:\n{final_all_emails}",'debug',GGV_SETTINGS.DEBUG_LOGS)
        except StaleElementReferenceException as e:
            self.Func.print_log(f"ERROR: {e}. Skip fetching emails...",'debug',GGV_SETTINGS.DEBUG_LOGS)
        return final_all_emails

    def load_item(self,item_data,item_selector):

        if self.TRANSLATE:
            # Translate before Loading Items....
            item_data = self.translate_text(item_data)

        data = ItemLoader(item = GgventuresItem(), selector = item_selector)
        data.add_value('university_name', self.static_name)
        data.add_value('university_contact_info',self.university_contact_info)
        data.add_value('logo',self.static_logo)
        data.add_value('event_name', item_data['event_name'])
        data.add_value('event_desc', item_data['event_desc'])
        data.add_value('event_date', item_data['event_date'])
        data.add_value('event_link', item_data['event_link'])
        data.add_value('event_time', item_data['event_time'])
        data.add_value('startups_name', item_data['startups_name'])
        data.add_value('startups_contact_info', item_data['startups_contact_info'])
        if item_data['startups_link']:
            logger.debug(f"'startup_links' is loaded...") if GGV_SETTINGS.DEBUG_LOGS else None
            data.add_value('startups_link', item_data['startups_link'])
        else:
            logger.debug(f"'startup_links' is empty. Using get_links_from_source...") if GGV_SETTINGS.DEBUG_LOGS else None
            data.add_value('startups_link', self.get_links_from_source())

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

            self.university_contact_info = f"{self.university_contact_info}\n{self.get_emails_from_source()}"



    def parse_code(self,response):
        pass

    def parse(self, response):
        try:
            self.get_university_contact_info(response)
            yield scrapy.Request(url=response.url,callback=self.eventbrite_API_call)
        except Exception as e:
            self.exception_handler(e)

    def desc_images(self,desc_xpath='',use_getter=True):
        try:
            if use_getter:
                temp_event_desc = self.getter.find_element(By.XPATH,desc_xpath)
            else:
                temp_event_desc = self.driver.find_element(By.XPATH,desc_xpath)
            list_images = "\n".join([str(x.get_attribute('src')) for x in temp_event_desc.find_elements(By.XPATH,'.//img')])
            return f"{temp_event_desc.get_attribute('textContent')} \nPicture Link(s):\n{list_images}"
        except NoSuchAttributeException as e:
            logger.debug("No image found on spider {self.name}... scraping text only...")
            return temp_event_desc.get_attribute('textContent')

    def alert_handler(self,alert_text='',alert_accept=True,alert_driver=None):
        try:
            self.Mth.WebDriverWait(alert_driver, 10).until(self.Mth.EC.alert_is_present(),alert_text)
            alert = alert_driver.switch_to.alert
            if alert_accept:
                alert.accept()
            else:
                alert.dismiss()
            self.Func.print_log(f"Alert found and accepted... Proceeding to scrape spider {self.name}")
        except self.Exc.TimeoutException as e:
            self.Func.print_log(f"No Alert found with text \"{alert_text}\" on spider {self.name}... Proceeding to scrape spider")


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


    def events_list(self,event_links_xpath:str,return_elements=False,link_attribute='href'):
        try:
            web_elements_list = WebDriverWait(self.driver,40).until(EC.presence_of_all_elements_located((By.XPATH,event_links_xpath)))
            logger.debug(f"Number of Event Links: {len(web_elements_list)}")
            if return_elements:
                return web_elements_list
            else:
                return [x.get_attribute(link_attribute) for x in web_elements_list]
        except self.Exc.TimeoutException as e:
            logger.debug(f'No Events Found --> {e}. Skipping.....')
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


    def multi_event_pages(self,num_of_pages=6,event_links_xpath='',next_page_xpath='',get_next_month=False,click_next_month=False,wait_after_loading=False,click_month_list_xpath="",run_script=False\
        ,page_element='',current_page_class='',next_page_set_xpath='',href_button_xpath="",base_site=""):

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
                logger.debug(f"No available events for this month : {e} ---> Skipping...........")

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
                        self.driver.get(next_month)
                    if click_next_month:
                        next_page_btn = WebDriverWait(self.driver,40).until(EC.element_to_be_clickable((By.XPATH,next_page_xpath)))
                        if run_script:
                            self.driver.execute_script("arguments[0].click();", next_page_btn)
                        else:
                            next_page_btn.click()
                    # next_month = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'Go to the next page of the results')]"))).get_attribute('href')
                if wait_after_loading:
                    time.sleep(10)
            except (TimeoutException,NoSuchElementException,IndexError) as e:
                logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
                break
            logger.debug(f"IN-PROGRESS: Pending Number of Event Links: {len(event_links)}")

        logger.debug(f"Number of Event Links: {len(event_links)}")
        return event_links


    def closed(self, reason):
        try:
            self.driver.quit()
            if self.USE_MULTI_DRIVER:
                self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping closed due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            tb_log = traceback.format_exc()
            logger.exception(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            err_message = f"{type(e).__name__}\n{tb_log}\n{e}"
            error_email(self.name,err_message)
