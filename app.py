# CREATED BY JOHN EARL COBAR

# ---------------- IMPORTS ----------------------------- #
import time, os, sys, json, re
start_time = round(time.time())

from datetime import datetime, timezone, timedelta
from os import environ

try:
    import schedule
except:
    os.system(f"{sys.executable} -m pip install schedule")
    import schedule

## ------------------ CUSTOM IMPORTS ------------------------ ##

from binaries import logger

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

# ----- SPIDERS ------- #
# from ggventures.spiders.usa_0001 import Usa0001Spider
spider_list = [
                    "usa-0001"
              ]

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
# process.crawl(Usa0001Spider)
# spider_list = [
#                 'usa-0001'
#                 ]

########## MAIN START ############
if __name__ == '__main__':
    logger.info('Start Golden Goose Ventures Scraping Bot')
    # while True:
    for spider in spider_list:
        # spider = 'usa-0001'
        os.system(f"scrapy crawl {spider}")
    # process.start()
    logger.info("END of BOT")
