# CREATED BY JOHN EARL COBAR

# ---------------- IMPORTS ----------------------------- #
import time, os, sys, json, re
start_time = round(time.time())

from datetime import datetime, timezone, timedelta
from spider_list import Load_Spiders
from os import environ

# --------------- INSTALL MISSING DEPENDENCIES ----------------- #
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


## ------------------ CUSTOM IMPORTS ------------------------ ##

from binaries import GGV_SETTINGS, logger, DropBox_INIT

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

spider_list = Load_Spiders()

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
        logger.error(f"{errmsg + str(e)}")
        logger.debug(f"Golden Goose Ventures BOT Failed. | Time Taken = {end_time} {datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')}")
    # logger.debug("\nExiting Program in 30 Seconds or You can close window ...")
    # try:
    #     time.sleep(30)
    # except KeyboardInterrupt:
    #     pass
    sys.exit(1)

########## MAIN START ############
if __name__ == '__main__':
    try:
        logger.info('Start Golden Goose Ventures Scraping Bot\n')
        logger.info(f"\n{GGV_SETTINGS}\n")
        logger.debug(f'Fetching current progress on Dropbox BOT_JSON file...\n')
        status = DropBox_INIT()
        logger.info(status)
        logger.info(f"Number of Pending Spiders: {len(spider_list)}")
        # while True:
        for spider in spider_list:
            # spider = 'usa-0001
            logger.info(f"IN PROGRESS: Crawling with {spider}....")
            os.system(f"scrapy crawl {spider}")
        # process.start()
        end_time = str(round(((time.time() - start_time) / float(60)), 2)) + ' minutes' if (time.time() - start_time > 60.0) else str(round(time.time() - start_time)) + ' seconds'
        logger.debug(f"Golden Goose Ventures BOT Finished successfully. | Time Taken = {end_time} {datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')}")
    except Exception as e:
        exception_handler("ERROR: ", e)
