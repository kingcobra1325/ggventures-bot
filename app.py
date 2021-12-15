# CREATED BY JOHN EARL COBAR

# ---------------- IMPORTS ----------------------------- #
import time, os, sys, logging, json, re
start_time = round(time.time())

from datetime import datetime, timezone, timedelta
from os import environ

try:
    import schedule
except:
    os.system(f"{sys.executable} -m pip install schedule")
    import schedule
try:
    import selenium
except:
    os.system(f"{sys.executable} -m pip install selenium")
    import selenium
try:
    import gspread
except:
    os.system(f"{sys.executable} -m pip install gspread")
    import gspread
try:
    import pandas as pd
except:
    os.system(f"{sys.executable} -m pip install pandas")
    import pandas as pd
try:
    import openpyxl
    from openpyxl.utils import get_column_letter
    from openpyxl.styles import *
except:
    os.system(f"{sys.executable} -m pip install openpyxl")
    import openpyxl
    from openpyxl.utils import get_column_letter
    from openpyxl.styles import *

## ------------------- SCRAPY IMPORTS ------------------------ ##

# ----- SPIDERS ------- #
from ggventures.spiders.US_AUkogodSB import UsAukogodsbSpider

## ------------- Global Vars --------------- ##
cwd = os.path.dirname(os.path.realpath(__file__))
tdt = datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')
td = datetime.now().strftime('%m-%d-%Y')

## -------------------- LOGGER SETUP ----------------------- ##
FORMAT = "%(levelname)s: Func-%(funcName)s : Line-%(lineno)d : %(message)s"
log_file_name = f"GGVENTURES_BOT_LOG.log"
log_file_path = os.path.join(cwd, log_file_name)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=log_file_path, mode="w", encoding="UTF-8")
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())

# ------------- BINARY INIT ----------------- #
if environ.get('DEPLOYED'):
    GOOGLE_CHROME_BIN = environ.get('GOOGLE_CHROME_BIN')
    CHROMEDRIVER_PATH = environ.get('CHROMEDRIVER_PATH')
else:
    GOOGLE_CHROME_BIN = 'C:\Pysourcecodes\chromium\chrome.exe'
    CHROMEDRIVER_PATH = 'C:\Pysourcecodes\chromium\chromedriver'
