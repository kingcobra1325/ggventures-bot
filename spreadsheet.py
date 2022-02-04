import os,sys

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

from binaries import logger, Google_Sheets, gs_APIError, gs_NoWS, default_all_df, default_country_df, default_error_df, developer_bot_email, ALL_EVENTS_SHEET


SPREADSHEET_MAIN = Google_Sheets()


def ReOrder_Sheets():
    while True:
        try:
            order = []
            list_of_worksheets = SPREADSHEET_MAIN.worksheets()
            logger.debug(f"List of Worksheets: {list_of_worksheets}")

            for worksheet in list_of_worksheets:

                logger.info(f"Worksheet Name --> {worksheet.title} type: {type(worksheet.title)}")

                if worksheet.title == 'ALL':
                    logger.info(f"ALL Worksheet detected...")
                    order.append(worksheet)
                if worksheet.title == 'ERRORS':
                    logger.info(f"ERRORS Worksheet detected...")
                    order.append(worksheet)
            if order:
                logger.debug(f"Processing Sheet Reorder....")
                SPREADSHEET_MAIN.reorder_worksheets(order)
            break
        except gs_APIError as e:
            raise


def Create_Default_Sheet(spreadsheet,name):

    column_range = 'A:M'
    column_range_row = 'A1:M1'
    num_cols = '13'

    if name == 'ALL':
        logger.debug(f"Name identified as {name}. Setting Blank DataFrame for ALL")
        df = default_all_df.copy()
    elif name == 'ERRORS':
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
            if name == 'ALL':
                set_column_width(worksheet, 'A', 150)
                set_column_width(worksheet, 'G', 600)
                set_column_width(worksheet, 'L', 350)
            elif name == 'ERRORS':
                set_column_width(worksheet, 'A', 150)
                set_column_width(worksheet, 'B', 900)
                set_column_width(worksheet, 'D', 400)
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

            worksheet.add_protected_range(column_range_row, developer_bot_email)
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


def Read_DataFrame_From_Sheet(Name):

    # spreadsheet = Google_Sheets()
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
    while True:
        try:
            prev_df = get_as_dataframe(worksheet)
            logger.info(f"Getting DataFrame from {Name}...")
            break
        except gs_APIError as e:
            logger.error(f"Error processing GSpread API Request --> {e}.")
            logger.debug(f"Waiting for 90 seconds before retrying request")
            sleep(90)

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
    country_df.drop_duplicates(subset=['Event Name','Event Date'],inplace=True)


    # COUNTRY
    Write_DataFrame_To_Sheet(country_worksheet, country_df)
    logger.info(f"Added DataFrame to {country} Sheet")


    # ------ ALL -------- #
    if ALL_EVENTS_SHEET:

        # Getting ALL Sheet / Dataframe

        all_df, all_worksheet = Read_DataFrame_From_Sheet('ALL')

        all_data = data
        all_data["Country"] = country

        all_df.loc[all_df.shape[0]] = all_data

        # SORT ITEMS BY DATE AND REMOVE DUPLICATES

        all_df["Last Updated"] = all_df["Last Updated"].astype('datetime64[ns]')
        all_df.sort_values(by='Last Updated', ascending = False, inplace=True)
        all_df.drop_duplicates(subset=['Event Name','Event Date'],inplace=True)

        # WRITE ALL DF TO SHEET

        Write_DataFrame_To_Sheet(all_worksheet, all_df)
        logger.info("Added DataFrame to ALL Sheet")



def Log_Error(data):

    # Getting ERRORS Sheet / Datafram
    error_df, error_worksheet = Read_DataFrame_From_Sheet('ERRORS')

    error_df.loc[error_df.shape[0]] = data

    # SORT ITEMS BY DATE AND REMOVE DUPLICATES

    error_df["Time"] = error_df["Time"].astype('datetime64[ns]')
    error_df.sort_values(by='Time', ascending = False, inplace=True)

    # WRITE ALL DF TO SHEET

    Write_DataFrame_To_Sheet(error_worksheet, error_df)
    logger.info("Added DataFrame to ERRORS Sheet")
