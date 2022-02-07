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

from binaries import CLEAN_DATA_PIPELINE, GOOGLE_API_RATE_LIMIT_EMAIL, logger, Google_Sheets, gs_APIError, gs_NoWS, UnpackItems

from spreadsheet import Read_DataFrame_From_Sheet, Add_Event
from bot_email import missing_info_email, error_email

from models import pipeline_re
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class CleanDataPipeline:

    def __init__(self):
        pass

    def create_connection(self):
        pass

    def process_item(self, item, spider):
        try:
            if CLEAN_DATA_PIPELINE:
                logger.info("PIPELINE: CLEANING DATA....")
                logger.info(f"PIPELINE: Currently processing {spider.name} scraped data:")

                # SET ITEM ADAPTER
                adapter = ItemAdapter(item)

                # CLEAN UNIVERSITY CONTACT INFORMATION
                logger.info("CLEANING 'university_contact_info'")
                if adapter.get('university_contact_info'):
                    logger.info(f"Processing --> {adapter.get('university_contact_info')}")
                    adapter['university_contact_info'] = pipeline_re.contact_info(data=str(adapter.get('university_contact_info')))
                    logger.info(f"Result --> {adapter.get('university_contact_info')}")

                # data = {
                #             "Last Updated" : datetime.utcnow(),
                #             "Event Name" : UnpackItems(item.get("event_name")),
                #             "Event Date" : UnpackItems(item.get("event_date")),
                #             "Event Time" : UnpackItems(item.get("event_time")),
                #             "Event Link" : UnpackItems(item.get("event_link")),
                #             "Event Description" : UnpackItems(item.get("event_desc")),
                #             "Startup Name(s)" : UnpackItems(item.get("startups_name")),
                #             "Startup Link(s)" : UnpackItems(item.get("startups_link")),
                #             "Startup Contact Info(s)" : UnpackItems(item.get("startups_contact_info")),
                #             "University Name" : UnpackItems(item.get("university_name")),
                #             "University Contact Info" : UnpackItems(item.get("university_contact_info")),
                #             "Logo" : UnpackItems(item.get("logo")),
                #             "SpiderName" : spider.name
                # }
            else:
                logger.info("PIPELINE: SKIPPED CLEANING DATA...")

            return item

        except Exception as e:
            logger.error(f"Experienced error on the CleanData Pipeline --> {e}. Sending Error Email Notification")
            error_email(spider.name,e)


class WriteDataPipeline:

    def __init__(self):
        pass

    def create_connection(self):
        pass

    def process_item(self, item, spider):
        try:
            logger.info("PIPELINE: WRITING DATA....")
            logger.info(f"PIPELINE: Currently processing {spider.name} scraped data:")
            logger.info(f"{item}")

            data = {
                        "Last Updated" : datetime.utcnow(),
                        "Event Name" : UnpackItems(item.get("event_name")),
                        "Event Date" : UnpackItems(item.get("event_date")),
                        "Event Time" : UnpackItems(item.get("event_time")),
                        "Event Link" : UnpackItems(item.get("event_link")),
                        "Event Description" : UnpackItems(item.get("event_desc")),
                        "Startup Name(s)" : UnpackItems(item.get("startups_name")),
                        "Startup Link(s)" : UnpackItems(item.get("startups_link")),
                        "Startup Contact Info(s)" : UnpackItems(item.get("startups_contact_info")),
                        "University Name" : UnpackItems(item.get("university_name")),
                        "University Contact Info" : item.get("university_contact_info"),
                        "Logo" : UnpackItems(item.get("logo")),
                        "SpiderName" : spider.name
            }

            # GET COUNTRY DF
            df, worksheet = Read_DataFrame_From_Sheet(spider.country)

            # ADD ITEM TO DF
            Add_Event(data=data,country_df=df,country_worksheet=worksheet,country=spider.country)

            return item
        except Exception as e:
            logger.error(f"Experienced error on the WriteData Pipeline --> {e}. Sending Error Email Notification")
            error_email(spider.name,e)
