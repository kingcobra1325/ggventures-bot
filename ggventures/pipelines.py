# Define your item pipelines here
#
import os,sys,traceback, gc
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime, timezone
from time import sleep

from openpyxl import Workbook

try:
    from scrapy.exceptions import DropItem
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install scrapy")
    from scrapy.exceptions import DropItem

try:
    import pandas as pd
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install pandas")
    import pandas as pd
try:
    import openpyxl
    from openpyxl.utils import get_column_letter
    from openpyxl.styles import *
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install openpyxl")
    import openpyxl
    from openpyxl.utils import get_column_letter
    from openpyxl.styles import *
try:
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
except ModuleNotFoundError as e:
    os.system(f"{sys.executable} -m pip install gspread_dataframe")
    from gspread_dataframe import get_as_dataframe, set_with_dataframe

from binaries import GGV_SETTINGS, Google_Sheets, gs_APIError, gs_NoWS, UnpackItems
from lib.baselogger import initialize_logger

from spreadsheet import Read_DataFrame_From_Sheet, Add_Event, Add_Startups_Event
from bot_email import missing_info_email, error_email

from models import pipeline_re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

logger = initialize_logger()

"""
Scraped Data Pipeline Order:
1. CleanDataPipeline
2. WriteDataPipeline
3. StartupsPipeline

Can easily be enabled or disabled via GGV_SETTINGS or
by ITEM_PIPELINES in settings.py
"""

class CleanDataPipeline:

    """
    First Pipeline:
    If CLEAN_EVENT_DATE is enabled,  it will clean the Event Date via regex.
    If CLEAN_EVENT_TIME is enabled,  it will clean the Event Time via regex.
    If CLEAN_CONTACT_INFO is enabled, it will filter the data for phone numbers and email addresses via regex        

    Regex Patterns are found on patterns.py
    """

    def process_item(self, item, spider):
        try:
            if GGV_SETTINGS.CLEAN_DATA_PIPELINE:
                logger.info("PIPELINE: CLEANING DATA....")
                logger.info(f"PIPELINE: Currently processing {spider.name} scraped data:")

                # SET ITEM ADAPTER
                adapter = ItemAdapter(item)

                # CLEAN EVENT DATE
                if GGV_SETTINGS.CLEAN_EVENT_DATE:
                    logger.info("PIPELINE: CLEANING 'event_date'")
                    if adapter.get('event_date'):
                        logger.info(f"PIPELINE: Processing --> {adapter.get('event_date')}")
                        event_date_result = pipeline_re.clean_date(data=str(adapter.get('event_date')))
                        if not event_date_result:
                            logger.debug("PIPELINE: 'event_date' after regex is empty... Getting contact info on 'event_name'")
                            event_date_result = pipeline_re.clean_date(data=str(adapter.get('event_name')))
                        adapter['event_date'] = event_date_result
                        logger.info(f"PIPELINE: Result 'event_date' --> {adapter.get('event_date')}")
                    else:
                        logger.debug("PIPELINE: 'event_date' empty...")

                # CLEAN EVENT TIME
                if GGV_SETTINGS.CLEAN_EVENT_TIME:
                    logger.info("PIPELINE: CLEANING 'event_time'")
                    if adapter.get('event_time'):
                        logger.info(f"PIPELINE: Processing --> {adapter.get('event_time')}")
                        adapter['event_time'] = pipeline_re.clean_time(data=str(adapter.get('event_time')))
                        logger.info(f"PIPELINE: Result 'event_time' --> {adapter.get('event_time')}")
                    else:
                        logger.debug("PIPELINE: 'event_time' empty...")
                        if adapter.get('event_date'):
                            logger.debug("Using 'event_date' data for 'event_time' info...\n")
                            logger.info(f"PIPELINE: Processing --> {adapter.get('event_date')}")
                            adapter['event_time'] = pipeline_re.clean_time(data=str(adapter.get('event_date')))
                            logger.info(f"PIPELINE: Result 'event_time' --> {adapter.get('event_time')}")

                # CLEAN UNIVERSITY CONTACT INFORMATION
                if GGV_SETTINGS.CLEAN_CONTACT_INFO:
                    logger.info("PIPELINE: CLEANING 'university_contact_info'")
                    if adapter.get('university_contact_info'):
                        logger.info(f"PIPELINE: Processing --> {adapter.get('university_contact_info')}")
                        adapter['university_contact_info'] = pipeline_re.contact_info(data=str(adapter.get('university_contact_info')))
                        logger.info(f"PIPELINE: Result 'university_contact_info' --> {adapter.get('university_contact_info')}")
                    else:
                        logger.debug("PIPELINE: 'university_contact_info' empty...")


            else:
                logger.info("PIPELINE: SKIPPED CLEANING DATA...")

            return item

        except Exception as e:
            tb_log = traceback.format_exc()
            logger.exception(f"Experienced error on the CleanData Pipeline --> {type(e).__name__}\n{e}. Sending Error Email Notification")
            err_message = f"{type(e).__name__}\n{tb_log}\n{e}"
            error_email(spider.name,err_message)


class WriteDataPipeline:
    """
    This Pipeline will write the scraped data to the Google Sheets via the API.
    Refer to speadsheets.py for more details    
    """

    def process_item(self, item, spider):
        try:
            logger.info("PIPELINE: WRITING DATA....")
            logger.info(f"PIPELINE: Currently processing {spider.name} scraped data:")
            # logger.info(f"{item}")

            # SET ITEM ADAPTER
            adapter = ItemAdapter(item)

            data = {
                        "Last Updated" : datetime.utcnow(),
                        "Event Name" : UnpackItems(adapter.get("event_name")),
                        "Event Date" : str(adapter.get("event_date")),
                        "Event Time" : str(adapter.get("event_time")),
                        "Event Link" : UnpackItems(adapter.get("event_link")),
                        "Event Description" : UnpackItems(adapter.get("event_desc"))[:5000],
                        "Startup Name(s)" : UnpackItems(adapter.get("startups_name")),
                        "Startup Link(s)" : UnpackItems(adapter.get("startups_link")),
                        "Startup Contact Info(s)" : UnpackItems(adapter.get("startups_contact_info")),
                        "University Name" : UnpackItems(adapter.get("university_name")),
                        "University Contact Info" : str(adapter.get("university_contact_info"))[:5000],
                        "Logo" : UnpackItems(adapter.get("logo")),
                        "SpiderName" : spider.name
            }

            # GET COUNTRY DF
            df, worksheet = Read_DataFrame_From_Sheet(spider.country)

            # ADD ITEM TO DF
            Add_Event(data=data,country_df=df,country_worksheet=worksheet,country=spider.country)

            del df, data, worksheet
            gc.collect()

            return item
        except Exception as e:
            tb_log = traceback.format_exc()
            logger.exception(f"Experienced error on the WriteData Pipeline --> {type(e).__name__}\n{e}. Sending Error Email Notification")
            err_message = f"{type(e).__name__}\n{tb_log}\n{e}"
            error_email(spider.name,err_message)

class StartupsPipeline:
    """
    When SORT_STARTUPS is enabled, it will check the Event's Title and Description
    using regex to check if it qualifies as a startup using the keywords on the
    keywords.json file on the DropBox API.
    Qualifying Events will be added to the STARTUPS Sheet else it will be
    dropped from the Pipeline    
    """

    def process_item(self, item, spider):
        try:
            # GET STARTUP EVENTS INFORMATION
            if GGV_SETTINGS.SORT_STARTUPS:
                logger.info("PIPELINE: SORTING STARTUPS EVENTS....")
                logger.info(f"PIPELINE: Currently processing {spider.name} scraped data:")

                # SET ITEM ADAPTER
                adapter = ItemAdapter(item)

                criteria_list = []

                # CHECK EVENT IF IT CONTAINS STARTUP KEYWORDS
                logger.debug(f"PIPELINE: Checking Data for KEYWORDS....")
                check_event_title, title_criteria = pipeline_re.sort_startups(data=str(adapter.get('event_name')))
                criteria_list.append(title_criteria) if check_event_title else None
                check_event_desc, desc_criteria = pipeline_re.sort_startups(data=str(adapter.get('event_desc')))
                criteria_list.append(desc_criteria) if check_event_desc else None
                logger.debug(f"PIPELINE: STARTUP KEYWORDS - Event Title: {check_event_title}")
                logger.debug(f"PIPELINE: STARTUP KEYWORDS - Event Desc: {check_event_desc}")

                if check_event_title or check_event_desc:
                    logger.info("PIPELINE: Event meets Startup Keywords criteria...\n")
                    criteria_result = '\n'.join(criteria_list)
                    logger.debug(f"PIPELINE: Criteria:\n{criteria_result}")

                    if adapter.get('event_desc'):

                        if not adapter.get('startups_name'):
                            logger.info("PIPELINE: Fetching Startup Name from Description...\n")
                            adapter["startups_name"] = pipeline_re.get_startup_name(data=str(adapter.get('event_desc')))
                            logger.info(f"PIPELINE: Result 'startups_name' --> {adapter.get('startups_name')}\n")
                        else:
                            logger.debug("PIPELINE: Existing data on 'startups_name'. No changes made.")

                        if not adapter.get('startups_link'):
                            logger.info("PIPELINE: Fetching Startup Links from Description...")
                            adapter["startups_link"] = pipeline_re.get_startup_links(data=str(adapter.get('event_desc')))
                            logger.info(f"PIPELINE: Result 'startups_link' --> {adapter.get('startups_link')}\n")
                        else:
                            logger.debug("PIPELINE: Existing data on 'startups_link'. No changes made.")

                        if not adapter.get('startups_contact_info'):
                            logger.debug("PIPELINE: No existing data on 'startups_contact_info'. Getting contact info on 'event_desc'")
                            adapter["startups_contact_info"] = pipeline_re.contact_info(data=str(adapter.get('event_desc')))
                        else:
                            logger.debug("PIPELINE: Existing data on 'startups_contact_info'. No changes made.")
                    else:
                        logger.debug("PIPELINE: 'event_desc' empty.")
                        logger.debug("PIPELINE: Item Startup Data returns as empty...")

                    data = {
                                "Last Updated" : datetime.utcnow(),
                                "Country" : spider.country,
                                "Event Name" : UnpackItems(adapter.get("event_name")),
                                "Event Date" : str(adapter.get("event_date")),
                                "Event Time" : str(adapter.get("event_time")),
                                "Event Link" : UnpackItems(adapter.get("event_link")),
                                "Event Description" : UnpackItems(adapter.get("event_desc"))[:50000],
                                "Startup Name(s)" : UnpackItems(adapter.get("startups_name")),
                                "Startup Link(s)" : UnpackItems(adapter.get("startups_link")),
                                "Startup Contact Info(s)" : UnpackItems(adapter.get("startups_contact_info")),
                                "University Name" : UnpackItems(adapter.get("university_name")),
                                "University Contact Info" : str(adapter.get("university_contact_info"))[:50000],
                                "Logo" : UnpackItems(adapter.get("logo")),
                                "Criteria Met" : criteria_result,
                                "SpiderName" : spider.name
                    }

                    # GET STARTUPS DF
                    df, worksheet = Read_DataFrame_From_Sheet('STARTUPS')

                    # ADD ITEM TO DF
                    Add_Startups_Event(data=data,startups_df=df,startups_worksheet=worksheet,country=spider.country)

                    del df, data, worksheet
                    gc.collect()

                else:
                    raise DropItem("PIPELINE: Event failed to meet Startup Keyword criteria...")
            else:
                logger.info("PIPELINE: SKIPPING SORTING STARTUPS EVENTS...")
            return item

        except DropItem as e:
            # logger.error("PIPELINE: Skipping Scraped Event Item...")
            raise DropItem("PIPELINE: Skipping Scraped Event Item...")
        except Exception as e:
            tb_log = traceback.format_exc()
            logger.exception(f"Experienced error on the Startups Pipeline --> {type(e).__name__}\n{e}. Sending Error Email Notification")
            err_message = f"{type(e).__name__}\n{tb_log}\n{e}"
            error_email(spider.name,err_message)
