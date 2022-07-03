# CREATED BY JOHN EARL COBAR

## --------------- INITIALIZE BASE CLASSES --------------- ##

"""
    Initialize main logger object and custom objects
"""

from lib.baselogger import initialize_logger
from lib.error_dashboard import ErrorDashboard
from lib.funcs import list_to_gen

logger = initialize_logger(__name__)

from lib.email_spreadsheet import EmailCopySheet

# ---------------- IMPORTS ----------------------------- #
from mimetypes import init
import time, os, sys, threading,gc
start_time = round(time.time())

from datetime import datetime
from spider_list import Load_Spiders
from spider_list_test import Load_Spiders_Test
from os import environ

# --------------- INSTALL MISSING DEPENDENCIES ---------- ------- #
try:
    from scrapy.exceptions import DropItem
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install scrapy")
    from scrapy.exceptions import DropItem
try:
    import schedule
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install schedule")
    import schedule
try:
    import tabulate
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install tabulate")
    import tabulate
try:
    from googletrans import Translator
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install googletrans==3.1.0a0")
    from googletrans import Translator

## ------------------ CUSTOM IMPORTS ------------------------ ##

    """
    Load binaries and env vars and settings
    """

from binaries import GGV_SETTINGS, DropBox_INIT, DropBox_Upload, restart_heroku_dynos
from spreadsheet import delete_past_events

## ------------------- SCRAPY IMPORTS ------------------------ ##

# try:
#     import scrapy
#     from scrapy.crawler import CrawlerProcess
#     from scrapy.settings import Settings
#     from ggventures import settings as my_settings
#
# except:
#     os.system(f"{sys.executable} -m pip install scrapy")
#     import scrapy
#     from scrapy.crawler import CrawlerProcess


## ------------- Global Vars --------------- ##
cwd = os.path.dirname(os.path.realpath(__file__))
tdt = datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')
td = datetime.now().strftime('%m-%d-%Y')

## --------------------- CRAWLER PROCESS ------------------------ ##

# crawler_settings = Settings()
# crawler_settings.setmodule(my_settings)
# process = CrawlerProcess(settings=crawler_settings)
# process = CrawlerProcess(settings = {
#                         'FEED_URI' : 'ggventures_data.csv',
#                         'FEED_FORMAT' : 'csv'
#                         })

## ---------------------- LOAD SPIDERS -------------------------- ##

def exception_handler(errmsg="", e=""):
    """
    Handle the Error Occur in the program
    :param errmsg: Error message
    :param e: error object
    :return: Update Logs and Exit Program
    """
    print(f"\n\n{'-'*51}")
    if type(e).__name__ == "KeyboardInterrupt":
        end_time = str(round(((time.time() - start_time) / float(60)), 2)) + ' minutes' if (
                time.time() - start_time > 60.0) else str(round(time.time() - start_time)) + ' seconds'
        logger.debug(f"Golden Goose Ventures BOT Failed. | Time Taken = {end_time}")
        logger.error("Program aborted by the user.")
    else:
        end_time = str(round(((time.time() - start_time) / float(60)), 2)) + ' minutes' if (time.time() - start_time > 60.0) else str(round(time.time() - start_time)) + ' seconds'
        logger.exception(f"{errmsg + str(e)}")
        logger.debug(f"Golden Goose Ventures BOT Failed. | Time Taken = {end_time} {datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')}")
    # logger.debug("\nExiting Program in 30 Seconds or You can close window ...")
    # try:
    #     time.sleep(30)
    # except KeyboardInterrupt:
    #     pass
    sys.exit(1)

def send_email():
    """
    Sends offline copy of spreadsheet via email
    :params: None
    :return: None
    """
    logger.info("Sending spreadsheet copies via Email...")
    email_offline = EmailCopySheet()
    email_offline.send_copy_via_email()
    del email_offline
    gc.collect()

# SCRAPING
def start_spiders():
    """
    Loads spiders from Dashboard if env 'GET_SPIDERLIST_FROM_DASHBOARD' is True
    else it will check GET_SPIDERLIST_FROM_DASHBOARD setting if its True

    If both are false, it will get the spiders from the spider_list.py if 'DEPLOYED'
    spider_list_test.py if not 'DEPLOYED'

    Pulls the spiders.json file on the Dropbox API and check if there are any 'PENDING_SPIDERS'
    Gets the List of 'PENDING_SPIDERS' if there are any to resume scraping
    else it will load a new list depending on which spider list is loaded from previously.
    """
    if environ.get("GET_SPIDERLIST_FROM_DASHBOARD",GGV_SETTINGS.GET_SPIDERLIST_FROM_DASHBOARD):
        logger.info("Loading Spiders from Dashboard....")
        error_dashboard = ErrorDashboard()
        get_spider_list = error_dashboard.get_spiders_on_status()
        del error_dashboard
        gc.collect()
    else:
        logger.debug("Fetching Spiders from local file...")
        if environ.get('DEPLOYED'):
            logger.info("|PRODUCTION| Loading Spider_List....")
            get_spider_list = Load_Spiders()
        else:
            logger.info("|DEVELOPMENT| Loading Spider_List_Test....")
            get_spider_list = Load_Spiders_Test()

    logger.info(f"Spider_List: {get_spider_list}")

    if GGV_SETTINGS.LOAD_DROPBOX_LIST:
        logger.debug(f'Fetching current progress on Dropbox BOT_JSON file...\n')
        load_spiders = DropBox_INIT()
        logger.info(load_spiders)
        if len(load_spiders["PENDING_SPIDERS"]) >= 1:
            logger.info("Pending Spiders to scrape detected. Resuming....")
            spider_list = load_spiders["PENDING_SPIDERS"]
        else:
            spider_list = get_spider_list
            logger.info("No Pending Spiders to resume. Scraping New Spider List....")
    else:
        logger.info("Resume Progress DISABLED. Scraping New Spider List....")
        spider_list = get_spider_list
    logger.info(f"Number of Pending Spiders: {len(spider_list)}")

    """
    Duplicates the spider list and creates a generator to iterate through to scrape
    Will run each iterated spider with the 'scrapy crawl' command line

    If the bot is not multi-threading while env 'DEPLOYED' is True:
    After all of the spiders are done being scraped. It will send an offline copy via email.

    Every spiders scraped will add onto a counter in which once its equal or greater than the
    settings 'DB_SAVE_SPIDER_COUNTER'. It will save the remaining spiders that has yet to be
    scraped onto the bot.json file into the Dropbox API.
    Also it do the following:
    It will 'DELETE_PAST_EVENTS' if the settings is True
    It restarts the Heroku Dynos if settings 'RESTART_HEROKU_EVERY_SAVESTATE' is True

    Once its done it will save an empty bot.json file onto the Dropbox API
    """

    progress_counter = 0
    save_counter = 0
    save_spider_list = spider_list.copy()
    spider_list = list_to_gen(spider_list)

    for spider in spider_list:
        # spider = 'usa-0001
        logger.info(f"IN PROGRESS: Crawling with {spider}....")
        os.system(f"scrapy crawl {spider}")
        progress_counter += 1
        save_counter += 1
        logger.debug(f"Save Progress Counter {save_counter}/{GGV_SETTINGS.DB_SAVE_SPIDER_COUNTER}")
        logger.info(f"Removing {spider} from Pending Spider List...")
        save_spider_list.remove(spider)
        if environ.get('DEPLOYED') and not environ.get('SCHEDULE_EMAIL_COPY') and environ.get('SEND_EMAIL_OFFLINE_COPY') and not len(save_spider_list):
            send_email()
        if (save_counter >= GGV_SETTINGS.DB_SAVE_SPIDER_COUNTER) and GGV_SETTINGS.SAVE_DROPBOX_LIST:
            logger.debug("Saving progress to Dropbox...")
            logger.debug(save_spider_list)
            DropBox_Upload(save_spider_list)
            save_counter = 0
            if GGV_SETTINGS.DELETE_PAST_EVENTS:
                delete_past_events()
            if environ.get('DEPLOYED') and GGV_SETTINGS.RESTART_HEROKU_EVERY_SAVESTATE:
                restart_heroku_dynos()
        logger.info(f"\n\nCURRENT SCRAPING PROGRESS: {progress_counter}\n\n")

    logger.info("Finished pending Spider List...")
    logger.debug("Saving empty list to Dropbox...")
    DropBox_Upload(save_spider_list)

"""
Schedules email offline copy every 'Saturday' at '12:00 NN' EST / '4:00 PM' UTC
"""
schedule.every().saturday.at("16:00").do(send_email)

# WORKERS

def email_spreadsheet_worker():
    """
    Email Worker Thread
    """
    logger.info("Initializing sending email copies every 'Monday'")
    while True:
        schedule.run_pending()

def ggventures_bot_worker():
    """
    Scrapy Worker Thread:
    If 'DEPLOYED' env is True: Runs the start_spiders function indefinitely
    else it will only run it once and the program will stop

    Also if its False with the Settings 'DELETE_PAST_EVENTS' enabled
    It will delete the past events on the spreadsheet

    Prints out the time once the program is finished
    """
    try:
        logger.info('Start Golden Goose Ventures Scraping Bot\n')
        logger.info(f"\n{GGV_SETTINGS}\n")

        if environ.get('DEPLOYED'):
            logger.info("|PRODUCTION| Running program indefinitely....")
            while True:
                start_spiders()
                logger.info("Completed current progress. Restarting Spider list...")
        else:
            logger.info("|DEVELOPMENT| Running program one-off....")
            start_spiders()
            if GGV_SETTINGS.DELETE_PAST_EVENTS:
                delete_past_events()
        # process.start()
        end_time = str(round(((time.time() - start_time) / float(60)), 2)) + ' minutes' if (time.time() - start_time > 60.0) else str(round(time.time() - start_time)) + ' seconds'
        logger.debug(f"Golden Goose Ventures BOT Finished successfully. | Time Taken = {end_time} {datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')}")
    except Exception as e:
        exception_handler("ERROR: ", e)


########## MAIN START ############
if __name__ == '__main__':
    """
    Starts multi-threading if 'SCHEDULE_EMAIL_COPY' env is True.
    Runs the ggventures_bot_worker only if False.
    """
    if environ.get('SCHEDULE_EMAIL_COPY'):
        # THREADS INIT
        scraping_t = threading.Thread(target=ggventures_bot_worker)
        email_copy_t = threading.Thread(target=email_spreadsheet_worker)
        # THREADS START
        scraping_t.start()
        email_copy_t.start()

        # THREADS JOIN
        scraping_t.join()
        email_copy_t.join()
    else:
        ggventures_bot_worker()
