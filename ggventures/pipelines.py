# Define your item pipelines here
#
import os,sys
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime, timezone
from time import sleep

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
try:
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
except:
    os.system(f"{sys.executable} -m pip install gspread_dataframe")
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
try:
    from gspread_formatting.dataframe import format_with_dataframe
    from gspread_formatting import *
    # from gspread_formatting import batch_updater
except:
    os.system(f"{sys.executable} -m pip install gspread_formatting")
    # from gspread_formatting import batch_updater
    from gspread_formatting import *
    from gspread_formatting.dataframe import format_with_dataframe

from binaries import logger, Google_Sheets, formatter, GetValueByIndex, gs_APIError, gs_NoWS, GOOGLE_API_RATE_LIMIT_EMAIL, Create_Default_Sheet
from bot_email import missing_info_email, error_email

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GgventuresPipeline:

    def __init__(self):
        pass

    def create_connection(self):
        pass

    def process_item(self, item, spider):
        try:
            logger.info(f"PIPELINE: Currently processing {spider.name} scraped data:")
            logger.info(f"{item}")
            df_all, spreadsheet = Google_Sheets()
            df = df_all
            while True:
                try:
                    try:
                        worksheet = spreadsheet.worksheet(spider.country)
                    except gs_NoWS as e:
                        logger.debug(f"Worksheet Not Found for -----> {spider.country}. Error: {e}")
                        logger.debug(f"Creating Worksheet {spider.country}")
                        worksheet = Create_Default_Sheet(spreadsheet,spider.country)
                    break
                except gs_APIError as e:
                    logger.error(f"Error processing GSpread API Request --> {e}.")
                    logger.debug(f"Waiting for 90 seconds before retrying request")
                    sleep(90)

            data = {
                        # "Last Updated" : datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p'),
                        "Last Updated" : datetime.utcnow(),
                        "Event Name" : GetValueByIndex(item.get("event_name"),0),
                        "Event Date" : GetValueByIndex(item.get("event_date"),0),
                        "Event Time" : GetValueByIndex(item.get("event_time"),0),
                        "Event Link" : GetValueByIndex(item.get("event_link"),0),
                        "Event Description" : GetValueByIndex(item.get("event_desc"),0),
                        "Startup Name(s)" : GetValueByIndex(item.get("startups_name"),0),
                        "Startup Link(s)" : GetValueByIndex(item.get("startups_link"),0),
                        "Startup Contact Info(s)" : GetValueByIndex(item.get("startups_contact_info"),0),
                        "University Name" : GetValueByIndex(item.get("university_name"),0),
                        "University Contact Info" : GetValueByIndex(item.get("university_contact_info"),0),
                        "Logo" : GetValueByIndex(item.get("logo"),0),
                        "SpiderName" : spider.name
            }
            # GET EXISTING DF from WORKSHEET
            retry = 0
            retry_max = 9
            while True:
                try:
                    prev_df = get_as_dataframe(worksheet)
                    break
                except gs_APIError as e:
                    if retry >= retry_max:
                        if GOOGLE_API_RATE_LIMIT_EMAIL:
                            logger.error(f"Error processing GSpread API Request --> {e}. Retries Exceeding more than {retry_max} attempts. Sending Error Email Notification")
                            error_email(spider.name,e)
                            retry = 0
                        else:
                            logger.error(f"Error processing GSpread API Request --> {e}.")
                            retry = 0
                    else:
                        logger.error(f"Error processing GSpread API Request --> {e}.")
                        retry+=1
                    logger.debug(f"Waiting for 90 seconds before retrying request")
                    sleep(90)
            df = prev_df.copy()
            # REMOVE EMPTY ROWS
            df.dropna(how='all',inplace=True)
            # ADD ITEM TO DF
            df.loc[df.shape[0]] = data
            # SORT ITEMS BY DATE AND REMOVE DUPLICATES
            df["Last Updated"] = df["Last Updated"].astype('datetime64[ns]')
            df.sort_values(by='Last Updated', ascending = False, inplace=True)
            df.drop_duplicates(subset=['Event Name','Event Date'],inplace=True)
            # WRITE DF TO GOOGGLE SHEETS
            retry = 0
            retry_max = 9
            while True:
                try:
                    try:
                        pass
                    except gs_NoSS as e:
                        logger.debug(f"Error: {e} ---> Worksheet ")
                    prev_df = set_with_dataframe(worksheet, df)
                    break
                except gs_APIError as e:
                    if retry >= retry_max:
                        if GOOGLE_API_RATE_LIMIT_EMAIL:
                            logger.error(f"Error processing GSpread API Request --> {e}. Sending Error Email Notification")
                            error_email(spider.name,e)
                            retry = 0
                        else:
                            logger.error(f"Error processing GSpread API Request --> {e}.")
                            retry = 0
                    else:
                        logger.error(f"Error processing GSpread API Request --> {e}.")
                        retry+=1
                    logger.debug(f"Waiting for 90 seconds before retrying request")
                    sleep(90)
            # format_with_dataframe(worksheet, df, formatter, include_column_header=True)
            return item
        except Exception as e:
            logger.error(f"Experienced error on the Pipeline --> {e}. Sending Error Email Notification")
            error_email(spider.name,e)
