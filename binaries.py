from __future__ import print_function
import time, os, sys, logging, json, ast
from os import environ
# try:
#     import redis
# except:
#     os.system(f"{sys.executable} -m pip install redis")
#     import redis
try:
    from dotenv import load_dotenv
except Exception as e:
    os.system(f"{sys.executable} -m pip install python-dotenv")
    from dotenv import load_dotenv
try:
    import gspread
    from gspread.exceptions import APIError as gs_APIError
    from gspread.exceptions import WorksheetNotFound as gs_NoWS
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install gspread")
    import gspread
    from gspread.exceptions import APIError as gs_APIError
    from gspread.exceptions import WorksheetNotFound as gs_NoWS
try:
    from eventbrite import Eventbrite
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install eventbrite")
    from eventbrite import Eventbrite

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import ChromeOptions
    from selenium.webdriver.firefox.options import FirefoxOptions
try:
    import pandas as pd
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install pandas")
    import pandas as pd
try:
    import dropbox
    from dropbox.exceptions import ApiError
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install dropbox")
    import dropbox
    from dropbox.exceptions import ApiError
try:
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install gspread_dataframe")
    from gspread_dataframe import get_as_dataframe, set_with_dataframe

try:
    import requests
except ModuleNotFoundError as e:
    os.system(f"pip install requests")
    import requests
# try:
#     import sib_api_v3_sdk
#     from sib_api_v3_sdk.rest import ApiException
# except:
#     os.system(f"{sys.executable} -m pip install sib_api_v3_sdk")
#     import sib_api_v3_sdk
#     from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

from lib.baselogger import initialize_logger
from lib.decorators import decorate

from patterns import STARTUP_EVENT_KEYWORDS, STARTUP_NAMES

################ LOAD ENV VARIABLES ####################

"""
    Loads env variables from .env file
"""

load_dotenv('.env')

"""
    Loads all of the Environmental Vars from '.env' file
    when running the code on a local system.
    Set each env vars to a corresponding variable
"""

# EMAIL VARS

SMTP_SERVER = environ['SMTP_SERVER']
SMTP_PORT = environ['SMTP_PORT']
SMTP_EMAIL = environ['SMTP_EMAIL']
SMTP_KEY = environ['SMTP_KEY']

# EVENTBRITE VARS

EB_API_KEY = environ['EB_API_KEY']
EB_CLIENT_SECRET = environ['EB_CLIENT_SECRET']
EB_PRIVATE_TOKEN = environ['EB_PRIVATE_TOKEN']
EB_PUBLIC_TOKEN = environ['EB_PUBLIC_TOKEN']

#  GSPREAD DEVELOPER VARS

if environ.get('DEPLOYED'):
    GOOGLE_SHEETS_API = environ['GOOGLE_SHEETS_API_MAIN']
    BOT_KEYS = ast.literal_eval(environ['BOT_KEYS_MAIN'])
    SPREADSHEET_ID = environ['SPREADSHEET_ID_MAIN']
    ERRORS_SPREADSHEET_ID = environ['ERRORS_SPREADSHEET_ID_MAIN']
else:
    GOOGLE_SHEETS_API = environ['GOOGLE_SHEETS_API_DEV']
    BOT_KEYS = ast.literal_eval(environ['BOT_KEYS_DEV'])
    SPREADSHEET_ID = environ['SPREADSHEET_ID_DEV']
    ERRORS_SPREADSHEET_ID = environ['ERRORS_SPREADSHEET_ID_DEV']

# DROPBOX VARS

if environ.get('DEPLOYED'):
    DROPBOX_TOKEN = environ['DROPBOX_TOKEN_MAIN']
else:
    DROPBOX_TOKEN = environ['DROPBOX_TOKEN_DEV']

# DEV / CLIENT EMAILS

if environ.get('DEPLOYED'):
    DEVELOPER_BOT_EMAIL = ast.literal_eval(environ['MAIN_BOT_EMAIL'])
else:
    DEVELOPER_BOT_EMAIL = ast.literal_eval(environ['DEVELOPER_BOT_EMAIL'])

DEVELOPER_EMAILS = ast.literal_eval(environ['DEVELOPER_EMAILS'])

EMAIL_OFFLINE_COPY = ast.literal_eval(environ['EMAIL_OFFLINE_COPY'])

# CHROME VARS

# if environ.get('DEPLOYED'):
    # DEPLOYED VARS
    # GOOGLE_CHROME_BIN = environ['GOOGLE_CHROME_BIN']
# CHROMEDRIVER_PATH = environ['CHROMEDRIVER_PATH']
# else:
#     # DEVELOPER VARS
#     GOOGLE_CHROME_BIN = environ['DEFAULT_GOOGLE_CHROME_BIN']
CHROMEDRIVER_PATH = environ['DEFAULT_CHROMEDRIVER_PATH']
GECKODRIVER_PATH = environ['DEFAULT_GECKODRIVER_PATH']

# HEROKU API TOKEN

HEROKU_API_TOKEN = environ['HEROKU_API_TOKEN']

############## SETTINGS ################


class APPSettings():

    """
    Settings object for the GGVentures scraping bot.
    Contains multiple attributes accessible that changes the
    behaviour of different functions on the bot
    """

    def __init__(self):

        # DEFAULT SETTINGS
        self.COUNTRY_EVENTS_SHEET = environ.get('COUNTRY_EVENTS_SHEET')
        self.ALL_EVENTS_SHEET = environ.get('ALL_EVENTS_SHEET')
        self.UNIQUE_EVENT_EMAILS = False
        self.GOOGLE_API_RATE_LIMIT_EMAIL = False
        self.CLEAN_DATA_PIPELINE = True
        # self.CLEAN_DATA_PIPELINE = False
        self.CLEAN_EVENT_DATE = True
        # self.CLEAN_EVENT_DATE = False
        self.CLEAN_EVENT_TIME = True
        self.CLEAN_CONTACT_INFO = True
        self.SORT_STARTUPS = True
        self.KEEP_UNIQUE_EVENTS = True
        self.LIMIT_SCRAPED_EMAILS=10
        self.LIMIT_SCRAPED_PHONENUMBERS=10
        # self.DELETE_PAST_EVENTS = True
        self.DELETE_PAST_EVENTS = environ.get('DEPLOYED')
        self.REGEX_LOGS = not environ.get('DEPLOYED')
        self.DEV_LOGS = True
        self.NO_MATCH_REGEX_LOGS = not environ.get('DEPLOYED')
        self.MULTI_DRIVER = False
        # self.GET_SPIDERLIST_FROM_DASHBOARD = True
        self.GET_SPIDERLIST_FROM_DASHBOARD = environ.get('DEPLOYED')
        # self.SEND_EMAIL_OFFLINE_COPY = True
        self.SEND_EMAIL_OFFLINE_COPY = False
        self.SEND_EMAILS_PER_ERROR = environ['SEND_EMAILS_PER_ERROR']
        self.RECORD_ERROR_COUNTER = True
        self.RESTART_HEROKU_EVERY_SAVESTATE = True
        self.GET_IMAGES_DESCRIPTION = False
        if environ.get('DEPLOYED'):
            self.LOAD_DROPBOX_LIST = True
            self.SAVE_DROPBOX_LIST = True
            self.REGEX_LOGS = False
            self.NO_MATCH_REGEX_LOGS = False
            self.DEBUG_LOGS = False
            self.DEV_LOGS = False
        else:
            self.LOAD_DROPBOX_LIST = False
            self.SAVE_DROPBOX_LIST = False
            self.DEBUG_LOGS = True
        self.DB_SAVE_SPIDER_COUNTER = 3
        self.FAIL_COUNTER = 10
        self.PRINT_ENV_VARS = False

    def __repr__(self):

        repr_string = ''
        for k,v in self.__dict__.items():
            repr_string = repr_string + f"{k} -> {v}\n"
        return repr_string

GGV_SETTINGS = APPSettings()

########################################

## -------------------- LOGGER SETUP ----------------------- ##

"""
    Initialize the logger 
"""
logger = initialize_logger()

def print_log(msg="",method='info',condition=True):
    if condition:
        if method.lower() == 'info':
            logger.info(msg)
        elif method.lower() == 'debug':
            logger.debug(msg)
        elif method.lower() == 'warning':
            logger.warning(msg)
        elif method.lower() == 'error':
            logger.error(msg)
        elif method.lower() == 'critical':
            logger.critical(msg)
        elif method.lower() == 'exception':
            logger.exception(msg)
        else:
            logger.exception(f"Invalid method |{method}|..")
    else:
        pass

# -------------------- PRINT ENV VARS -------------------------- #

if GGV_SETTINGS.PRINT_ENV_VARS:
    logger.debug("\nLOADED ENV VARS...\n")
    logger.debug(f"SMTP_SERVER -> {SMTP_SERVER}")
    logger.debug(f"SMTP_PORT -> {SMTP_PORT}")
    logger.debug(f"SMTP_EMAIL -> {SMTP_EMAIL}")
    logger.debug(f"SMTP_KEY -> {SMTP_KEY}")
    logger.debug(f"EB_API_KEY -> {EB_API_KEY}")
    logger.debug(f"EB_CLIENT_SECRET -> {EB_CLIENT_SECRET}")
    logger.debug(f"EB_PRIVATE_TOKEN -> {EB_PRIVATE_TOKEN}")
    logger.debug(f"EB_PUBLIC_TOKEN -> {EB_PUBLIC_TOKEN}")
    logger.debug(f"GOOGLE_SHEETS_API -> {GOOGLE_SHEETS_API}")
    logger.debug(f"BOT_KEYS -> {BOT_KEYS}")
    logger.debug(f"SPREADSHEET_ID -> {SPREADSHEET_ID}")
    logger.debug(f"DROPBOX_TOKEN -> {DROPBOX_TOKEN}")
    logger.debug(f"DEVELOPER_BOT_EMAIL -> {DEVELOPER_BOT_EMAIL}")
    logger.debug(f"DEVELOPER_EMAILS -> {DEVELOPER_EMAILS}")
    # logger.debug(f"GOOGLE_CHROME_BIN -> {GOOGLE_CHROME_BIN}")
    logger.debug(f"CHROMEDRIVER_PATH -> {CHROMEDRIVER_PATH}")


def EventBrite_API():
    """
    Calls the Eventbrite API using the Private Token to access the service
    :return: Eventbrite object
    """
    return Eventbrite(EB_PRIVATE_TOKEN)

################################# DATAFRAME ###################################################

"""
    Set the different dataframes to be used
    in the GGVentures bot.
"""

default_all_df = pd.DataFrame(columns=["Last Updated", "Country", "Event Name", "Event Date", "Event Time", "Event Link", "Event Description", "Startup Name(s)",
                                "Startup Link(s)", "Startup Contact Info(s)", "University Name", "University Contact Info", "Logo", "SpiderName"])

default_startups_df = pd.DataFrame(columns=["Last Updated", "Country", "Event Name", "Event Date", "Event Time", "Event Link", "Event Description", "Startup Name(s)",
                                "Startup Link(s)", "Startup Contact Info(s)", "University Name", "University Contact Info", "Logo", "Criteria Met", "SpiderName"])

default_country_df = pd.DataFrame(columns=["Last Updated", "Event Name", "Event Date", "Event Time", "Event Link", "Event Description", "Startup Name(s)",
                                "Startup Link(s)", "Startup Contact Info(s)", "University Name", "University Contact Info", "Logo", "SpiderName"])

default_dashboard_df = pd.DataFrame(columns=["Last Updated","Spider","Status","Consecutive Fail Count","Last Error Time"])

default_error_df = pd.DataFrame(columns=["Time", "Error", "SpiderName", "Status"])


######################### GOOGLE API #############################################

@decorate.connection_retry()
def Google_Sheets():
    """
    Create a gspread object with the 'Service Account' API 
    key to access different Google API Services.
    Access the Google Sheets identified by 'SPREADSHEET_ID'
    :return: spreadsheet gspread object
    """
    gc = gspread.service_account_from_dict(BOT_KEYS)
    return gc.open_by_key(SPREADSHEET_ID)

############################## SELENIUM #########################################

##### -------------------------- CHROMEDRIVER ------------------------------####

def Load_ChromeDriver():
    """
    Creates a Chrome WebDriver Object to be used
    for loading JS websites. Loads parameters
    to run the browser in headless mode.
    :return: WebDriver object
    """
    options = ChromeOptions()
    # ------------- DRIVER OPTIONS --------------- #
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("--log-level=3")
    options.add_argument("--lang=en-US")
    # options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--no-sandbox')
    options.add_argument("--enable-features=NetworkServiceInProcess")
    prefs = {
                'intl.accept_languages' : 'en-US'
            }
    options.add_experimental_option("prefs",prefs)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # driver.set_page_load_timeout(1000)

    return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=options)

#### ------------------------- FIREFOX --------------------------------------####

# # ------------- BINARY INIT ----------------- #
# if environ.get('DEPLOYED'):
#     FIRE_FOX_BIN = environ.get('FIRE_FOX_BIN')
#     GECKODRIVER_PATH = environ.get('GECKODRIVER_PATH')
# else:
#     # DEVELOPER VARS
#     FIRE_FOX_BIN = 'C:\\Pysourcecodes\\Firefox\\firefox.exe'
#     GECKODRIVER_PATH = 'C:\\Pysourcecodes\\Firefox\\geckodriver'
#
def Load_FF_Driver():
#     # ------------- DRIVER OPTIONS --------------- #
    options = FirefoxOptions()
#     # ------------- DRIVER OPTIONS --------------- #
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument(f'user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--log-level=3")
    options.add_argument("--lang=en-US")
    # options.binary_location = FIRE_FOX_BIN
    options.add_argument('--no-sandbox')
#
    return webdriver.Chrome(executable_path=GECKODRIVER_PATH,options=options)

# DRIVER VAR
def Load_Driver(USE_FF_DRIVER=False):
    if USE_FF_DRIVER:
        return Load_FF_Driver()
    return Load_ChromeDriver()
    

####################################### DROPBOX ###########################################

# API Access for Modules
@decorate.connection_retry()
def DropBox_Upload(upload):
    """
    Saves the pending spiders list
    to the DropBox API as bot.json 
    :param upload: pending spiders list
    """
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    while True:
        try:
            json_data = {
                            'PENDING_SPIDERS' : upload
                        }

            with open('bot.json', 'w') as data:
                json.dump(json_data, data)
            logger.info("Finished writing data to local json file...")
            with open('bot.json', 'rb') as data:
                dbx.files_upload(data.read(),'/bot.json',dropbox.files.WriteMode.overwrite)
            logger.info("Progress uploaded successfully...")
            break
        except (ApiError,AttributeError):
            pass



# API Access for Main APP
@decorate.connection_retry()
def DropBox_INIT():
    """
    Creates a Dropbox object with the Token to connect 
    to the Dropbox API. Downloads the bot.json file
    from the API. If not found, creates a bot.json file
    with an empty pending spider list to upload to it.
    :return: pending_spiders list
    """
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    try:
        # Download DROPBOX File
        downloaded = dbx.files_download_to_file('bot.json','/bot.json')
        return json.loads(open('bot.json').read())
    except (ApiError,AttributeError):
        while True:
            logger.error('Bot JSON not found!...')
            # Delete Local File Copy
            try:
                os.remove('bot.json')
                logger.error('Deleting Local Copy...')
            except FileNotFoundError:
                pass
            # Create local EMPTY File
            with open('bot.json', 'w') as data:
                # json_data = {
                #                 'PENDING_SPIDERS' : [],
                #                 'PAGE_SOURCES' : {}
                #             }
                json_data = {
                                'PENDING_SPIDERS' : []
                            }
                json.dump(json_data, data)
                logger.debug('Creating Blank Copy...')
            # Upload EMPTY Copy to the DROPBOX API
            with open('bot.json', 'rb') as data:
                dbx.files_upload(data.read(),'/bot.json',dropbox.files.WriteMode.overwrite)
                logger.debug('Uploading Blank Copy...')
            break
        return json_data

@decorate.connection_retry()
def DropBox_Keywords():
    """
    Creates a DropBox API using the Token to pull the data
    from the keywords.json file. If not found, creates a
    keywords.json file with a templates from patterns.py.
    :return: Keywords dict from keywords.json file
    """
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    try:
        logger.info("Loading Startup Keywords Criteria from DropBox...")
        # Download DROPBOX File
        downloaded = dbx.files_download_to_file('keywords.json','/keywords.json')
        # return json.loads(open('keywords.json').read())
        result = json.loads(open('keywords.json').read())
        logger.info(result)
        return result
    except (ApiError,AttributeError):
        while True:
            logger.error('Bot JSON not found!...')
            # Delete Local File Copy
            try:
                os.remove('keywords.json')
                logger.error('Deleting Local Copy...')
            except FileNotFoundError:
                pass
            # Create local EMPTY File
            with open('keywords.json', 'w') as data:

                json_data = STARTUP_EVENT_KEYWORDS

                json.dump(json_data, data)
                logger.debug('Creating Blank Copy...')
            # Upload EMPTY Copy to the DROPBOX API
            with open('keywords.json', 'rb') as data:
                dbx.files_upload(data.read(),'/keywords.json',dropbox.files.WriteMode.overwrite)
                logger.debug('Uploading Blank Copy...')
            break
        logger.info(json_data)
        return json_data

@decorate.connection_retry()
def DropBox_EventNames():
    """
    Creates DropBox API object to pull the startups.json file
    If not found, creates a blank file to upload to DropBox.
    :return: startups list from startups.json
    """
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    try:
        # Download DROPBOX File
        logger.info("Loading Startup Event Names from DropBox...")
        downloaded = dbx.files_download_to_file('startups.json','/startups.json')
        # return json.loads(open('startups.json').read())
        result = json.loads(open('startups.json').read())
        logger.info(result)
        return result
    except (ApiError,AttributeError):
        while True:
            logger.error('Bot JSON not found!...')
            # Delete Local File Copy
            try:
                os.remove('startups.json')
                logger.error('Deleting Local Copy...')
            except FileNotFoundError:
                pass
            # Create local EMPTY File
            with open('startups.json', 'w') as data:

                json_data = STARTUP_NAMES

                json.dump(json_data, data)
                logger.debug('Creating Blank Copy...')
            # Upload EMPTY Copy to the DROPBOX API
            with open('startups.json', 'rb') as data:
                dbx.files_upload(data.read(),'/startups.json',dropbox.files.WriteMode.overwrite)
                logger.debug('Uploading Blank Copy...')
            break
        logger.info(json_data)
        return json_data







####################################### FUNCTIONS #########################################

@decorate.connection_retry()
def restart_heroku_dynos():
        """
        Perform 'DELETE' API request to Heroku API
        to restart all of the dynos tied to the
        GGVentures Bot deployed
        """
        logger.critical("\nRestarting Heroku Dynos...\n")
        headersList = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {HEROKU_API_TOKEN}" 
        }
        response = requests.delete("https://api.heroku.com/apps/ggventures/dynos",headers=headersList)
        logger.critical(f"Heroku Response: {response}...")

def WebScroller(driver,height=10):
    for i in range(0,height,int(height/10)):
        driver.execute_script("window.scrollBy(0, {0});".format(i))
        time.sleep(0.1)

def UnpackItems(item):
    """
    :param item: list/dict item
    :return: index 0 from item
    """
    if item:
        try:
            return "\n".join(item)
        except (KeyError,TypeError) as e:
            logger.info(f"Error {e}: Unable to get value from index")
            return ''
    else:
        return ''


# --------------- ERROR EXCEPTION ----------------- #

# def exception_handler(errmsg="", e="",start_time):
#     """
#     Handle the Error Occur in the program
#     :param errmsg: Error message
#     :param e: error object
#     :return: Update Logs and Exit Program
#     """
#     print(f"\n\n{'-'*51}")
#     if type(e).__name__ == "KeyboardInterrupt":
#         end_time = str(round(((time.time() - start_time) / float(60)), 2)) + ' minutes' if (
#                 time.time() - start_time > 60.0) else str(round(time.time() - start_time)) + ' seconds'
#         logger.debug(f"Golden Goose Ventures BOT Failed. | Time Taken = {end_time}")
#         logger.error("Program aborted by the user.")
#     else:
#         end_time = str(round(((time.time() - start_time) / float(60)), 2)) + ' minutes' if (time.time() - start_time > 60.0) else str(round(time.time() - start_time)) + ' seconds'
#         logger.error(f"{errmsg + str(e)}")
#         logger.debug(f"Golden Goose Ventures BOT Failed. | Time Taken = {end_time}")
#     # logger.debug("\nExiting Program in 30 Seconds or You can close window ...")
#     # try:
#     #     time.sleep(30)
#     # except KeyboardInterrupt:
#     #     pass
#     sys.exit(1)
