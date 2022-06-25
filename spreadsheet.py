import os,sys,pytz,gc

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
    from gspread_formatting import set_column_width
except:
    os.system(f"{sys.executable} -m pip install gspread_formatting")
    from gspread_formatting import set_column_width

from binaries import Google_Sheets, gs_APIError, gs_NoWS, default_dashboard_df, default_all_df, default_startups_df, default_country_df, default_error_df, DEVELOPER_BOT_EMAIL, GGV_SETTINGS
from lib.baselogger import initialize_logger

SPREADSHEET_MAIN = Google_Sheets()

logger = initialize_logger()

def check_outdated_events(date_list):
    bool_array = []
    logger.debug(f"\nEvent Date: |{date_list}|{type(date_list)}|\n")
    current_date = datetime.now(pytz.timezone('Pacific/Honolulu')).replace(hour=0, minute=0, second=0, microsecond=0)
    for event_date in list(date_list):
        event_bool = True
        for raw in event_date:
            try:
                logger.debug(f"\nRaw Date: |{raw}|{type(raw)}|\n")
                logger.debug(f"Using MM/DD/YYYY Strptime Pattern...")
                date = datetime.strptime(raw,'%m/%d/%Y').replace(tzinfo=pytz.utc)
                logger.debug(f"\nStripped Date: |{date.strftime('%m-%d-%Y')}|{type(raw)}|\n")
            except ValueError as e:
                try:
                    logger.debug(f"MM/DD/YYYY not valid. Using MM/DD Strptime Pattern...")
                    date = datetime.strptime(raw,'%m/%d').replace(year=datetime.now().year,tzinfo=pytz.utc)
                    logger.debug(f"\nStripped Date: |{date.strftime('%m-%d-%Y')}|{type(raw)}|\n")
                except ValueError as e:
                    logger.debug(f"No valid data to strip time {e}. Skipping...")
                    continue
            if current_date <= date:
                logger.debug(f"Event Date |{date.strftime('%m-%d-%Y')}| is equal/later than Current Date |{current_date.strftime('%m-%d-%Y')}|...")
                event_bool = False
                logger.debug(f"{event_date} -> FALSE\n")
            else:
                logger.debug(f"Event Date |{date.strftime('%m-%d-%Y')}| is no longer a valid date...")
        bool_array.append(event_bool)
        if event_bool:
            logger.debug(f"{event_date} -> TRUE\n")
    logger.debug(f"\nFinal Bool Array: |{bool_array}|\n")
    logger.debug(f"\nDate List Count -> |{len(date_list)}| Bool Array Count -> |{len(bool_array)}|\n")
    logger.info(f"\nNumber of Deleted Rows: |{bool_array.count(True)}|\n")
    return bool_array

def ReOrder_Sheets():
    while True:
        try:
            order = []
            list_of_worksheets = SPREADSHEET_MAIN.worksheets()
            logger.debug(f"List of Worksheets: {list_of_worksheets}")

            for worksheet in list_of_worksheets:

                logger.info(f"Worksheet Name --> {worksheet.title} type: {type(worksheet.title)}")

                if worksheet.title == 'STARTUPS':
                    logger.info(f"STARTUPS Worksheet detected...")
                    order.append(worksheet)

            for worksheet in list_of_worksheets:

                if worksheet.title == 'ALL':
                    logger.info(f"ALL Worksheet detected...")
                    order.append(worksheet)
            
            for worksheet in list_of_worksheets:

                if worksheet.title == 'DASHBOARD':
                    logger.info(f"DASHBOARD Worksheet detected...")
                    order.append(worksheet)

            for worksheet in list_of_worksheets:

                if worksheet.title == 'ERRORS':
                    logger.info(f"ERRORS Worksheet detected...")
                    order.append(worksheet)
            if order:
                logger.debug(f"Processing Sheet Reorder....")
                SPREADSHEET_MAIN.reorder_worksheets(order)
            break
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)


def Create_Default_Sheet(spreadsheet,name):

    column_range = 'A:M'
    column_range_row = 'A1:M1'
    num_cols = '13'

    if name == 'ALL':
        logger.debug(f"Name identified as {name}. Setting Blank DataFrame for ALL")
        df = default_all_df.copy()
        # print(len(df.columns))
        # print(df.to_markdown())
        column_range = 'A:N'
        column_range_row = 'A1:N1'
        num_cols = '14'
    elif name == 'STARTUPS':
        logger.debug(f"Name identified as {name}. Setting Blank DataFrame for STARTUPS")
        df = default_startups_df.copy()
        column_range = 'A:O'
        column_range_row = 'A1:O1'
        num_cols = '15'
    elif name == 'DASHBOARD':
        logger.debug(f"Name identified as {name}. Setting Blank DataFrame for DASHBOARD")
        df = default_dashboard_df.copy()
        column_range = 'A:E'
        column_range_row = 'A1:E1'
        num_cols = '5'
    elif name == 'ERRORS':
        column_range = 'A:D'
        column_range_row = 'A1:D1'
        num_cols = '4'
        logger.debug(f"Name identified as {name}. Setting Blank DataFrame for ERRORS")
        df = default_error_df.copy()
        column_range = 'A:D'
        column_range_row = 'A1:D1'
        num_cols = '4'
    else:
        logger.debug(f"Name identified as {name}. Setting Blank DataFrame for Country")
        df = default_country_df.copy()

    while True:
        try:
            worksheet = spreadsheet.add_worksheet(title=name, rows="5000", cols=num_cols)
            break
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)

    while True:
        try:

            # Set Event Description and University Contact Info COLUMN Size
            if name == 'ALL' or name == 'STARTUPS':
                set_column_width(worksheet, 'A', 150)
                set_column_width(worksheet, 'G', 600)
                set_column_width(worksheet, 'L', 350)
            elif name == 'ERRORS':
                set_column_width(worksheet, 'A', 150)
                set_column_width(worksheet, 'B', 900)
                set_column_width(worksheet, 'D', 400)
            elif name == 'DASHBOARD':
                set_column_width(worksheet, 'A', 150)
                set_column_width(worksheet, 'C', 150)
                set_column_width(worksheet, 'D', 200)
                set_column_width(worksheet, 'E', 150)
            else:
                set_column_width(worksheet, 'A', 150)
                set_column_width(worksheet, 'F', 600)
                set_column_width(worksheet, 'K', 350)

            worksheet.format(column_range,{"wrapStrategy":"WRAP"})
            worksheet.freeze(rows=1)

            worksheet.format(column_range_row, {
                                                    "backgroundColor": {
                                                                          "red": 0.0,
                                                                          "green": 0.0,
                                                                          "blue": 0.0
                                                                        },
                                                    "horizontalAlignment": "CENTER",
                                                    'textFormat': {
                                                                    "foregroundColor": {
                                                                                            "red": 1.0,
                                                                                            "green": 1.0,
                                                                                            "blue": 1.0
                                                                                          },
                                                                    'bold': True
                                                                    }
                                                })

            worksheet.add_protected_range(column_range_row, DEVELOPER_BOT_EMAIL)
            set_with_dataframe(worksheet, df)
            logger.info(f"Added Blank Dataframe for {name}")
            break
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)

    ReOrder_Sheets()
    return worksheet


def Write_DataFrame_To_Sheet(worksheet,df):
    while True:
        try:
            # try:
            #     pass
            # except gs_NoSS as e:
            #     logger.debug(f"Error: {e} ---> Worksheet ")
            set_with_dataframe(worksheet, df)
            logger.info(f"Added DataFrame into Sheet")
            break
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)


def get_dataframe(Name,worksheet):
    while True:
        try:
            prev_df = get_as_dataframe(worksheet)
            logger.info(f"Getting DataFrame from {Name}...")
            return prev_df
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)

def Read_DataFrame_From_Sheet(Name,spreadsheet=False):

    # spreadsheet = Google_Sheets()
    if not spreadsheet:
        spreadsheet = SPREADSHEET_MAIN

    # Fetching / Creating Spreadsheet
    while True:
        try:
            try:
                worksheet = spreadsheet.worksheet(Name)
                logger.info(f"Getting Worksheet {Name}...")
            except gs_NoWS as e:
                logger.debug(f"Worksheet Not Found for -----> {Name}. Error: {e}")
                logger.debug(f"Creating Worksheet {Name}")
                worksheet = Create_Default_Sheet(spreadsheet,Name)
            break
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)

    # Getting DataFrame from Sheet
    prev_df = get_dataframe(Name,worksheet)

    df = prev_df.copy()
    # REMOVE EMPTY ROWS
    df.dropna(how='all',inplace=True)

    return df, worksheet

def Add_Event(data,country_df,country_worksheet,country):

    # ------ COUNTRY -------- #

    # Adding Scraped Event to DFs

    country_df.loc[country_df.shape[0]] = data

    # SORT ITEMS BY DATE AND REMOVE DUPLICATES
    country_df["Last Updated"] = country_df["Last Updated"].astype('datetime64[ns]')
    country_df.sort_values(by='Last Updated', ascending = False, inplace=True)
    country_df.drop_duplicates(subset=['Event Name','Event Date'],keep='last',inplace=True)

    # DELETE PAST EVENTS
    if GGV_SETTINGS.DELETE_PAST_EVENTS:
        col_dates_list = country_df["Event Date"].astype('str').apply(lambda x: x.split(" - "))
        country_df.drop(col_dates_list[check_outdated_events(col_dates_list)].index,inplace=True)
        del [col_dates_list]


    # COUNTRY
    Write_DataFrame_To_Sheet(country_worksheet, country_df)
    logger.info(f"Added DataFrame to {country} Sheet")
    del [country_df]


    # ------ ALL -------- #
    if GGV_SETTINGS.ALL_EVENTS_SHEET:

        # Getting ALL Sheet / Dataframe

        all_df, all_worksheet = Read_DataFrame_From_Sheet('ALL')

        all_data = data
        all_data["Country"] = country

        all_df.loc[all_df.shape[0]] = all_data

        # SORT ITEMS BY DATE AND REMOVE DUPLICATES

        all_df["Last Updated"] = all_df["Last Updated"].astype('datetime64[ns]')
        all_df.sort_values(by='Last Updated', ascending = False, inplace=True)
        all_df.drop_duplicates(subset=['Event Name','Event Date'],keep='last',inplace=True)

        # DELETE PAST EVENTS
        if GGV_SETTINGS.DELETE_PAST_EVENTS:
            col_dates_list = all_df["Event Date"].astype('str').apply(lambda x: x.split(" - "))
            all_df.drop(col_dates_list[check_outdated_events(col_dates_list)].index,inplace=True)
            del [col_dates_list]

        # WRITE ALL DF TO SHEET

        Write_DataFrame_To_Sheet(all_worksheet, all_df)
        logger.info("Added DataFrame to ALL Sheet")
        del [all_df]

    gc.collect()


def Add_Startups_Event(data,startups_df,startups_worksheet,country):

    # Adding Sorted Startup Events to DF

    startups_df.loc[startups_df.shape[0]] = data

    # SORT ITEMS BY DATE AND REMOVE DUPLICATES
    startups_df["Last Updated"] = startups_df["Last Updated"].astype('datetime64[ns]')
    startups_df.sort_values(by='Last Updated', ascending = False, inplace=True)
    startups_df.drop_duplicates(subset=['Event Name','Event Date'],keep='last',inplace=True)

    # DELETE PAST EVENTS
    if GGV_SETTINGS.DELETE_PAST_EVENTS:
        col_dates_list = startups_df["Event Date"].astype('str').apply(lambda x: x.split(" - "))
        startups_df.drop(col_dates_list[check_outdated_events(col_dates_list)].index,inplace=True)
        del [col_dates_list]


    # STARTUPS
    Write_DataFrame_To_Sheet(startups_worksheet, startups_df)
    logger.info(f"Added DataFrame to STARTUPS Sheet")

    del [startups_df]
    gc.collect()
