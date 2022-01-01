from __future__ import print_function
import time, os, sys, logging, json
from os import environ
# try:
#     import redis
# except:
#     os.system(f"{sys.executable} -m pip install redis")
#     import redis
try:
    import gspread
    from gspread.exceptions import APIError as gs_APIError
except:
    os.system(f"{sys.executable} -m pip install gspread")
    import gspread
    from gspread.exceptions import APIError as gs_APIError
try:
    from eventbrite import Eventbrite
except:
    os.system(f"{sys.executable} -m pip install eventbrite")
    from eventbrite import Eventbrite

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
except:
    os.system(f"{sys.executable} -m pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import ChromeOptions
    from selenium.webdriver.firefox.options import FirefoxOptions
try:
    import pandas as pd
except:
    os.system(f"{sys.executable} -m pip install pandas")
    import pandas as pd
try:
    import dropbox
    from dropbox.exceptions import ApiError
except:
    os.system(f"{sys.executable} -m pip install dropbox")
    import dropbox
    from dropbox.exceptions import ApiError
try:
    from gspread_formatting.dataframe import BasicFormatter, Color
except:
    os.system(f"{sys.executable} -m pip install gspread_formatting")
    from gspread_formatting.dataframe import BasicFormatter, Color

# try:
#     import sib_api_v3_sdk
#     from sib_api_v3_sdk.rest import ApiException
# except:
#     os.system(f"{sys.executable} -m pip install sib_api_v3_sdk")
#     import sib_api_v3_sdk
#     from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


## -------------------- LOGGER SETUP ----------------------- ##
cwd = os.path.dirname(os.path.realpath(__file__))
FORMAT = "%(levelname)s: Func-%(funcName)s : Line-%(lineno)d : %(message)s"
log_file_name = f"GGVENTURES_BOT_LOG.log"
log_file_path = os.path.join(cwd, log_file_name)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=log_file_path, mode="w", encoding="UTF-8")
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())

## ----------------------- EMAIL API KEY ----------------------------- ##

if environ.get('DEPLOYED'):
    # BOT_EMAIL_API_KEY = environ.get('EMAIL_API_KEY')
    SMTP_SERVER = environ.get('SMTP_SERVER')
    SMTP_PORT = environ.get('SMTP_PORT')
    SMTP_EMAIL = environ.get('SMTP_EMAIL')
    SMTP_KEY = environ.get('SMTP_KEY')
else:
    # DEVELOPER TOKEN
    # BOT_EMAIL_API_KEY = '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'
    SMTP_SERVER = 'smtp-relay.sendinblue.com'
    SMTP_PORT = '587'
    SMTP_EMAIL = 'goldengooseventures.developer@gmail.com'
    SMTP_KEY = 'zdFnEt7j56JgbOR0'

## -------------------- EVENTBRITE ---------------------------------- ##

if environ.get('DEPLOYED'):
    EB_API_KEY = environ.get('EB_API_KEY')
    EB_CLIENT_SECRET = environ.get('EB_CLIENT_SECRET')
    EB_PRIVATE_TOKEN = environ.get('EB_PRIVATE_TOKEN')
    EB_PUBLIC_TOKEN = environ.get('EB_PUBLIC_TOKEN')
else:
    # DEVELOPER TOKEN
    EB_API_KEY = 'FZ3N5FJX7CBHPQ5BV6'
    EB_CLIENT_SECRET = 'QQXGTE6QDA55I6BC2JEGLR2WJW525T7ACWRAHQEHMPCWASCPLY'
    EB_PRIVATE_TOKEN = 'PRMPUINSBIOQFJYEDFSR'
    EB_PUBLIC_TOKEN = 'NIUZTJJG4HQTETQ5IRQG'

def EventBrite_API():
    return Eventbrite(EB_PRIVATE_TOKEN)

################################# DATAFRAME ###################################################

df = pd.DataFrame(columns=["Last Updated", "Event Name", "Event Date", "Event Time", "Event Link", "Event Description", "Startup Name(s)",
                                "Startup Link(s)", "Startup Contact Info(s)", "University Name", "University Contact Info", "Logo", "SpiderName"])


######################### GOOGLE API #############################################

GOOGLE_SHEETS_API = 'AIzaSyCWiS836ydyMyWSwIK2jmpAwYogXGv3zNQ'

# DEVELOPER ID
SPREADSHEET_ID = '1I_ITHd6vn7x0Qil1wiX98G_t8dkcicBf1r-9Dik7GUY'

if environ.get('DEPLOYED'):
    BOT_KEYS = environ.get('BOT_KEYS')
else:
    # DEVELOPER VARS
    BOT_KEYS = {
      "type": "service_account",
      "project_id": "ggventures",
      "private_key_id": "33307ac49480497f17de746108a5bc27bc25b496",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCc064qlEOWsWkA\nS/UbZx6bgueMgpaQZKEKK3aQmJ/NS9wdOXlsHiqrg9rtsRnAph8nCfB0VpFpZpFC\nF2cb7Feh+1XiE+cX10ccxObs8xpdL+NrsujiToUCs1tTXDkXjc0LRwF5+hegG5L4\nxR3LDZ0tULx1VpuznHoMSlpPjnSwQGaw9TiriaCPNVXbhneKehqXfewJ3COYUc3M\n5dOyJKugn7sLI3tp5DpYtiU7abFOUHIRmIhym9RDZ8kw1lkRiZbQ6czAd3gPFJww\nzCk8LgBjzx/19IB87ZpyQhbxv7ZUw9mN/+ZEgSTWdHh4NTQhaPnhwgSGoyF5tmBe\n5SFolWzDAgMBAAECggEABPZRtCPdgPQmHWNJ4yRqfIMyLmj8uJ7mgDrgf9zEbwDa\neyDpbaQFYkiZccdBHa5j8p6cOXd6bGUEGEeYn0flfJ5GQ7wGJjlNP7ofOxofbcQT\nzxbpytdZ2rxaxGgjn6eAoxMLwen0O2sD8H5+3dZAG0H1ue9pR8/zW1Yy8KzSQQ1h\nN4gIJJj7IqEotfSHutQXJ433ULlb/n51fe4EhSlMuUgQ0lPAdavhcg1+pUflpbwk\n+6kBpdGVd4nX1M7SHBHoVBz/82FGxwgnBCizGoTm5CjETY1qNMDCqgjOlVpwW5D3\nrtxgiDh3XAH6QCgHqDPSmXPz2VMdFOD/9XLjACjQ+QKBgQDa/ypMTycK/CdsvHgN\n3z7h8Bvn6n79EFxAv2pD1yeMg77Ses+KeEh6NDymV6XpyfK//HzGRmM92AvmUmPl\nMTpJ2FPyJak/ug8k9IWbMclNC+dYypYGUnE+FDYNhiSWqoqMhZWHp6u5dLQszanN\np42vdFXbJt19uXkev2vR6BtdvQKBgQC3U1IP4PVHehSeDEMAXEjtOhIzCBzTQntL\nFLQWxGtL+lZ2xiozBWaxS5NLG77PF9XkJWfO/gVm1XLtHhF4VYFqGnQFG58AH34d\nSD6Ujny5I1tQXk6/CCuHrvlRs+fITQSY0B0UrEP2KqZMJLpq7sodNa1ZPVVUabBV\nm6p4urpcfwKBgQCQu80Hq9RA5U9lBNZPTLjxd8/poUgWFibyP8+KUHr52eRWlQXv\nHPnBkh53TTwA3BAMJGGOZNyX9d4/dTpCMhu0zD0Gry9BR8VUhip63BePTQuz2gf2\n26ut/IuQupQZ41I39t1RT1Yl9mRRrAbKPS9dwwQvF2uQ+PB8isRGcSEM/QKBgQCy\nArj7bDAf0L42XaetsO6rU6kaXnVG+hYoaJkaRm39n77XpEKTulnmLIGA/BcClp19\n5IhxaR2rpfXrozfJhhWdBsTDtPdmsi3OlzkVHWqkh12Co6CJRJCoNtIncK7PQ2IE\nVIj4avGvFejWpQ9TCD2/sUB7F+BEkD/GUNpuUrrlVwKBgFN9CRX1avwBRG1R4crh\n3fyd9q9eLzR5yD0+z1odr5LpbK66DxyHUb4kF8QbYWdu7sZyb2Jpn1lRZt9fwnN+\nIOF/ioYtLmLiNn9J2krb/F1m5oi1+FIuBEO4q9XDwN/2OvbJ4PNUIUCIrWRo7PvR\nSfGZ8k1T4/MM4F1/GHSj2uEI\n-----END PRIVATE KEY-----\n",
      "client_email": "ggventures-dev@ggventures.iam.gserviceaccount.com",
      "client_id": "112885207965191858762",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ggventures-dev%40ggventures.iam.gserviceaccount.com"
    }

formatter = BasicFormatter(
    header_background_color=Color(0,0,0),
    header_text_color=Color(1,1,1),
    decimal_format='#,##0.00'
)


def Google_Sheets():
    gc = gspread.service_account_from_dict(BOT_KEYS)
    return df, gc.open_by_key(SPREADSHEET_ID)

############################## SELENIUM #########################################

##### -------------------------- CHROMEDRIVER ------------------------------####
# ------------- BINARY INIT ----------------- #
if environ.get('DEPLOYED'):
    GOOGLE_CHROME_BIN = environ.get('GOOGLE_CHROME_BIN')
    CHROMEDRIVER_PATH = environ.get('CHROMEDRIVER_PATH')
else:
    # DEVELOPER VARS
    GOOGLE_CHROME_BIN = 'C:\\Pysourcecodes\\chromium\\chrome.exe'
    CHROMEDRIVER_PATH = 'C:\\Pysourcecodes\\chromium\\chromedriver'

# DRIVER VAR
def Load_Driver():
    options = ChromeOptions()
    # ------------- DRIVER OPTIONS --------------- #
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--log-level=3")
    options.add_argument("--lang=en-US")
    options.binary_location = GOOGLE_CHROME_BIN
    # options.add_argument('--no-sandbox')
    prefs = {
                'intl.accept_languages' : 'en-US'
            }
    options.add_experimental_option("prefs",prefs)

    return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=options)
# default_driver.quit()

#### ------------------------- FIREFOX --------------------------------------####

# ------------- BINARY INIT ----------------- #
if environ.get('DEPLOYED'):
    FIRE_FOX_BIN = environ.get('FIRE_FOX_BIN')
    GECKODRIVER_PATH = environ.get('GECKODRIVER_PATH')
else:
    # DEVELOPER VARS
    FIRE_FOX_BIN = 'C:\\Pysourcecodes\\Firefox\\firefox.exe'
    GECKODRIVER_PATH = 'C:\\Pysourcecodes\\Firefox\\geckodriver'

def Load_FF_Driver():
    # ------------- DRIVER OPTIONS --------------- #
    options = FirefoxOptions()
    # ------------- DRIVER OPTIONS --------------- #
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--log-level=3")
    options.add_argument("--lang=en-US")
    options.binary_location = FIRE_FOX_BIN
    # options.add_argument('--no-sandbox')

    return webdriver.Chrome(executable_path=GECKODRIVER_PATH,options=options)

####################################### DROPBOX ###########################################

# ------------- BINARY INIT ----------------- #
if environ.get('DEPLOYED'):
    DROPBOX_TOKEN = environ.get('DROPBOX_TOKEN')
else:
    # DEVELOPER TOKEN
    # DROPBOX_TOKEN = "zu4qdcxiutlxerm"
    DROPBOX_TOKEN = '87eVygKutx8AAAAAAAAAAdm1QXEJPIKBKiDndoKSeGGRq5WKKZ7dNA9_3r8Ic4Mg'
    # DROPBOX_TOKEN = 'ujw9jgy3f4hkn3l'

# API Access for Modules
def DropBox_Upload(json_file):
    return dropbox.Dropbox(DROPBOX_TOKEN)

# API Access for Main APP
def DropBox_INIT():
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    try:
        # Download DROPBOX File
        downloaded = dbx.files_download_to_file('bot_json.json','/bot_json.json')
        return json.loads(open('bot_json.json').read())
    except (ApiError,AttributeError):
        while True:
            logger.error('Bot JSON not found!...')
            # Delete Local File Copy
            try:
                os.remove('bot_json.json')
                logger.error('Deleting Local Copy...')
            except FileNotFoundError:
                pass
            # Create local EMPTY File
            with open('bot_json.json', 'w') as data:
                json_data = {
                                'PENDING_SPIDERS' : [],
                                'PAGE_SOURCES' : {}
                            }
                json.dump(json_data, data)
                logger.debug('Creating Blank Copy...')
            # Upload EMPTY Copy to the DROPBOX API
            with open('bot_json.json', 'rb') as data:
                dbx.files_upload(data.read(),'/bot_json.json',dropbox.files.WriteMode.overwrite)
                logger.debug('Uploading Blank Copy...')
            break
        return json_data




####################################### FUNCTIONS #########################################

def WebScroller(driver,height):
    for i in range(0,height,int(height/10)):
        driver.execute_script("window.scrollBy(0, {0});".format(i))
        time.sleep(0.5)

def GetValueByIndex(list,index):
    try:
        return list[index]
    except (KeyError,TypeError) as e:
        logger.info(f"Error {e}: Unable to get value from index")
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
