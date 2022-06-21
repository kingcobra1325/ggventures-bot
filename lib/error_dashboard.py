from cProfile import run
import os, json, gc

try:
    import dropbox
    from dropbox.exceptions import ApiError as DBApiError
except ModuleNotFoundError as e:
    os.system(f"pip install dropbox")
    import dropbox
    from dropbox.exceptions import ApiError as DBApiError
try:
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
except ModuleNotFoundError as e:
    os.system(f"pip install gspread_dataframe")
    from gspread_dataframe import get_as_dataframe, set_with_dataframe

try:
    import pandas as pd
except ModuleNotFoundError as e:
    os.system(f"pip install pandas")
    import pandas as pd
try:
    import gspread
    from gspread.exceptions import APIError as gs_APIError
    from gspread.exceptions import WorksheetNotFound as gs_NoWS
except ModuleNotFoundError as e:
    os.system(f"pip install gspread")
    import gspread
    from gspread.exceptions import APIError as gs_APIError
    from gspread.exceptions import WorksheetNotFound as gs_NoWS

from lib.baselogger import LoggerMixin
from binaries import ERRORS_SPREADSHEET_ID, BOT_KEYS, DROPBOX_TOKEN
from spreadsheet import Read_DataFrame_From_Sheet, Write_DataFrame_To_Sheet

class ErrorDashboard(LoggerMixin):

    def __init__(self):
        self.logger.debug("Initializing Errors Dashboard GSheet...")
        self.gc = gspread.service_account_from_dict(BOT_KEYS)
        self.spreadsheet = self.gc.open_by_key(ERRORS_SPREADSHEET_ID)
    
    def log_error(self,data):

        # Getting ERRORS Sheet / Datafram
        error_df, error_worksheet = Read_DataFrame_From_Sheet('ERRORS',self.spreadsheet)

        error_df.loc[error_df.shape[0]] = data

        # SORT ITEMS BY DATE AND REMOVE DUPLICATES

        error_df["Time"] = error_df["Time"].astype('datetime64[ns]')
        error_df.sort_values(by='Time', ascending = False, inplace=True)

        # WRITE ALL DF TO SHEET

        Write_DataFrame_To_Sheet(error_worksheet, error_df)
        self.logger.info("Added DataFrame to ERRORS Sheet")

    def read_dashboard(self):
        self.dashboard_df, self.dashboard_ws = Read_DataFrame_From_Sheet('DASHBOARD',self.spreadsheet)
        self.logger.info("Fetched Dashboard DataFrame from Worksheet...")

    def update_dashboard(self):
        Write_DataFrame_To_Sheet(self.dashboard_ws, self.dashboard_df)
        self.logger.info("Updated Dashboard Worksheet...")

    def delete_dashboard_dataframe(self):
        del self.dashboard_df
        gc.collect()
        self.logger.debug("Deleted Dashboard Dataframe...")

    def get_spiders_on_status(self,status='RUNNING'):
        self.read_dashboard()
        spiders = list(self.dashboard_df.loc[self.dashboard_df['Status']==status]['Spider'])
        self.delete_dashboard_dataframe()
        self.logger.info(f"Fetching Spiders based on status |{status}|")
        self.logger.debug(f"Fetched Spiders:\n{spiders}")
        self.logger.debug(f"Fetched Spiders Count: {len(spiders)}")
        return spiders
        


    # def DropBox_Keywords(self):
    #     dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    #     try:
    #         self.logger.info("Loading Startup Keywords Criteria from DropBox...")
    #         # Download DROPBOX File
    #         downloaded = dbx.files_download_to_file('keywords.json','/keywords.json')
    #         # return json.loads(open('keywords.json').read())
    #         result = json.loads(open('keywords.json').read())
    #         self.logger.info(result)
    #         return result
    #     except (DBApiError,AttributeError):
    #         while True:
    #             self.logger.error('Bot JSON not found!...')
    #             # Delete Local File Copy
    #             try:
    #                 os.remove('keywords.json')
    #                 self.logger.error('Deleting Local Copy...')
    #             except FileNotFoundError:
    #                 pass
    #             # Create local EMPTY File
    #             with open('keywords.json', 'w') as data:

    #                 json_data = STARTUP_EVENT_KEYWORDS

    #                 json.dump(json_data, data)
    #                 self.logger.debug('Creating Blank Copy...')
    #             # Upload EMPTY Copy to the DROPBOX API
    #             with open('keywords.json', 'rb') as data:
    #                 dbx.files_upload(data.read(),'/keywords.json',dropbox.files.WriteMode.overwrite)
    #                 self.logger.debug('Uploading Blank Copy...')
    #             break
    #         self.logger.info(json_data)
    #         return json_data

error_dashboard = ErrorDashboard()
