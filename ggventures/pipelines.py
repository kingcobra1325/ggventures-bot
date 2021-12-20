# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime, timezone

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
except:
    os.system(f"{sys.executable} -m pip install gspread_formatting")
    from gspread_formatting.dataframe import format_with_dataframe

from binaries import logger, Google_Sheets, remove_dup, formatter

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GgventuresPipeline:

    def __init__(self):
        pass

    def create_connection(self):
        pass

    def process_item(self, item, spider):
        print(f"PIPELINE: Currently processing {spider.name} scraped data:")
        print(f"{item}")
        df_all, spreadsheet = Google_Sheets()
        df = df_all
        worksheet = spreadsheet.worksheet(spider.country)
        data = {
                    "Last Updated" : datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p'),
                    "Event Name" : item.get("event_name"),
                    "Event Date" : item.get("event_date"),
                    "Event Time" : item.get("event_time"),
                    "Event Link" : item.get("event_link"),
                    "Event Description" : item.get("event_desc"),
                    "Startup Name(s)" : item.get("startups_name"),
                    "Startup Link(s)" : item.get("startups_link"),
                    "Startup Contact Info(s)" : item.get("startups_contact_info"),
                    "University Name" : item.get("university_name"),
                    "University Contact Info" : item.get("university_contact_info"),
                    "Logo" : item.get("logo"),
                    "SpiderName" : spider.name
        }
        df.loc[df.shape[0]] = data
        # GET EXISTING DF from WORKSHEET
        prev_df = get_as_dataframe(worksheet)
        # CHECK DUPLICATES AND ADD NEW DATA
        # df_diff = remove_dup(df,prev_df)
        # df.append(df_diff)
        # LOAD DATA INTO GOOGLE SHEETS
        set_with_dataframe(worksheet, df)
        format_with_dataframe(worksheet, df, formatter, include_column_header=True)
        return item
