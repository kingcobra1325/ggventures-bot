from cProfile import run
from collections import Counter
import os, json, gc

from datetime import datetime

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
from binaries import GGV_SETTINGS,ERRORS_SPREADSHEET_ID, BOT_KEYS, DROPBOX_TOKEN
from spreadsheet import Read_DataFrame_From_Sheet, Write_DataFrame_To_Sheet

class ErrorDashboard(LoggerMixin):

    def __init__(self):
        self.logger.debug("Initializing Errors Dashboard GSheet...")
        self.gc = gspread.service_account_from_dict(BOT_KEYS)
        self.spreadsheet = self.gc.open_by_key(ERRORS_SPREADSHEET_ID)

    def process_spider_status(self,spider_name,result='success'):
        self.logger.info("Processing Spider status after scraping...")
        self.logger.debug(f"Result |{result}|")
        self.read_dashboard()
        if result.lower() == 'success':
            self.clear_error_counter(spider_name,to_running_status=True,update_ws=False)
        else:
            self.log_error_counter(spider_name,update_ws=False)
        self.update_dashboard()
        self.delete_dashboard_dataframe()

    def get_spiders_on_status(self,status='RUNNING'):
        self.read_dashboard()
        spiders = list(self.dashboard_df.loc[self.dashboard_df['Status']==status]['Spider'])
        self.delete_dashboard_dataframe()
        # LOG OUTPUT
        self.logger.info(f"Fetching Spiders based on status |{status}|")
        self.logger.debug(f"Fetched Spiders:\n{spiders}")
        self.logger.debug(f"Fetched Spiders Count: {len(spiders)}")
        return spiders
        
    def log_error_counter(self,spider_name,update_ws=True):
        spider = self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name]
        fail_counter = f"{spider['Consecutive Fail Count'].values[0]}X"
        fail_num = Counter(fail_counter)['X']
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Consecutive Fail Count'] = fail_counter.replace("nan","")
        current_time = datetime.utcnow()
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Last Updated'] = current_time
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Last Error Time'] = current_time
        # LOG OUTPUT
        self.logger.debug(self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name])
        self.logger.info(f"Spider [{spider_name}] fail counter: {fail_num}")
        if fail_num >= GGV_SETTINGS.FAIL_COUNTER:
            self.logger.error("Fail Counter reached Threshold...")
            self.logger.debug(f"Fail Counter {fail_num} >= Threshold {GGV_SETTINGS.FAIL_COUNTER}")
            self.switch_spider_status(spider_name,update_ws=False)
        if update_ws:
            self.update_dashboard()
        
    def clear_error_counter(self,spider_name,to_running_status=False,update_ws=True):
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Consecutive Fail Count'] = ""
        current_time = datetime.utcnow()
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Last Updated'] = current_time
        current_status = self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Status'].values[0]
        # LOG OUTPUT
        self.logger.debug(self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name])
        self.logger.info(f"Cleared spider [{spider_name}] fail counter")
        if current_status == 'ERROR' and to_running_status:
            self.logger.info(f"Switching status of {spider_name} to |RUNNING|")
            self.switch_spider_status(spider_name,"RUNNING",update_ws=False)
        if update_ws:
            self.update_dashboard()

    def switch_spider_status(self,spider_name,status="ERROR",update_ws=True):
        orig_status = self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Status'].values[0]
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Status'] = status
        current_time = datetime.utcnow()
        self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name,'Last Updated'] = current_time
        # LOG OUTPUT
        self.logger.debug(self.dashboard_df.loc[self.dashboard_df['Spider']==spider_name])
        self.logger.debug(f"State Change |{orig_status}| -> |{status}|")
        self.logger.info(f"Changed [{spider_name}] status to |{status}|")
        if update_ws:
            self.update_dashboard()
    
    def log_error(self,data):
        # Getting ERRORS Sheet / Datafram
        error_df, error_worksheet = Read_DataFrame_From_Sheet('ERRORS',self.spreadsheet)
        error_df.loc[error_df.shape[0]] = data
        # SORT ITEMS BY DATE AND REMOVE DUPLICATES
        error_df["Time"] = error_df["Time"].astype('datetime64[ns]')
        error_df.sort_values(by='Time', ascending = False, inplace=True)
        # WRITE ALL DF TO SHEET
        Write_DataFrame_To_Sheet(error_worksheet, error_df)
        self.logger.info("ERRORs Sheet Updated...")

    def read_dashboard(self):
        self.dashboard_df, self.dashboard_ws = Read_DataFrame_From_Sheet('DASHBOARD',self.spreadsheet)
        self.logger.info("Fetched Dashboard DataFrame from Worksheet...")

    def update_dashboard(self):
        Write_DataFrame_To_Sheet(self.dashboard_ws, self.dashboard_df)
        self.logger.info("Dashboard Updated...")

    def delete_dashboard_dataframe(self):
        del self.dashboard_df
        gc.collect()
        self.logger.debug("Deleted Dashboard Dataframe...")



