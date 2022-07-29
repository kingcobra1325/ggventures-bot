from mimetypes import init
import scrapy, time, re

from datetime import datetime

from binaries import GGV_SETTINGS, DropBox_Keywords, DropBox_EventNames, Load_Driver, WebScroller, EventBrite_API
from lib.baselogger import initialize_logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import patterns

logger = initialize_logger()

class RegExGGV:
    """
    The Class that contains all of the regex and datetime functions
    """

    def __init__(self):
        self.re = re
        self.REGEX_LOGS = GGV_SETTINGS.REGEX_LOGS
        self.NO_MATCH_REGEX_LOGS = GGV_SETTINGS.NO_MATCH_REGEX_LOGS
        # PATTERNS VAR
        # self.STARTUP_EVENT_KEYWORDS = patterns.STARTUP_EVENT_KEYWORDS
        self.STARTUP_EVENT_KEYWORDS = DropBox_Keywords()
        # self.STARTUP_NAMES = patterns.STARTUP_NAMES
        self.STARTUP_NAMES = DropBox_EventNames()
        self.STARTUP_LINK_PATTERNS = patterns.STARTUP_LINK_PATTERNS
        self.TZ_PATTERNS = patterns.TZ_PATTERNS
        self.PHONE_NUMBER_PATTERNS = patterns.PHONE_NUMBER_PATTERNS
        self.EMAIL_PATTERNS = patterns.EMAIL_PATTERNS
        self.DATE_PATTERNS = patterns.DATE_PATTERNS
        self.DATE_PATTERNS_RE = patterns.DATE_PATTERNS_RE
        self.TIME_PATTERNS = patterns.TIME_PATTERNS
        self.TIME_PATTERNS_RE = patterns.TIME_PATTERNS_RE
        self.TZ_PATTERNS = patterns.TZ_PATTERNS
        self.TZ_EXCLUDE = patterns.TZ_EXCLUDE
        self.AM_PATTERNS = patterns.AM_PATTERNS
        self.PM_PATTERNS = patterns.PM_PATTERNS

    def perform_regex(self,pattern,data,method='all'):
        """
        Method to perform a regex function on the data/string that
        is processed with thee pattern str/list criteria
        :params: pattern -> list/str | data -> str | method -> str
        :return: regex results
        """
        if method == 'all':
            return self.re.compile('|'.join(pattern)).findall(data)
        if method == 'single':
            return self.re.compile(pattern).findall(data)
        else:
            raise Exception(f"Invalid Perform Regex Method |{method}| ....")

    def perform_strptime(self,pattern,strp_re,data,method='date'):

        final_data = ''
        final_data_ls = []

        fetch_date = self.perform_regex(strp_re,data)

        logger.info(f"Data after Regex ---> {fetch_date}")

        for fetch in fetch_date:
            for ptrn in pattern:

                if fetch.lower() == 'noon' and method == 'time':

                    logger.info(f"\nData detected as Noon. Setting Datetime to Noon and append...\n") if self.REGEX_LOGS else None
                    final_data_ls.append(datetime(year=datetime.now().year,month=datetime.now().month,day=datetime.now().day,hour=12).strftime('%I:%M:%S %p'))

                elif fetch.lower() == 'midnight' and method == 'time':

                    logger.info(f"\nData detected as Noon. Setting Datetime to Noon and append...\n") if self.REGEX_LOGS else None
                    final_data_ls.append(datetime(year=datetime.now().year,month=datetime.now().month,day=datetime.now().day,hour=23,minute=59,second=59).strftime('%I:%M:%S %p'))

                else:

                    data_process = ''
                    timezone_data = ''

                    try:
                        logger.info(f"Data : '{fetch}' | STRP : {ptrn[0]} | STRF : {ptrn[1]}") if self.REGEX_LOGS else None

                        if method == 'time':

                            # CLEAN AM-PM
                            for am_ptrn in self.AM_PATTERNS:
                                if am_ptrn in fetch:
                                    logger.info("Cleaning AM") if self.REGEX_LOGS else None

                                    fetch = fetch.replace(am_ptrn,"AM")

                                    logger.debug(f"Result --> {fetch}") if self.REGEX_LOGS else None
                            for pm_ptrn in self.PM_PATTERNS:
                                if pm_ptrn in fetch:
                                    logger.info("Cleaning PM") if self.REGEX_LOGS else None

                                    fetch = fetch.replace(pm_ptrn,"PM")

                                    logger.debug(f"Result --> {fetch}") if self.REGEX_LOGS else None


                            logger.info("Checking Time Data for valid timezone...") if self.REGEX_LOGS else None

                            try:
                                timezone_data = self.perform_regex(self.TZ_PATTERNS,fetch)
                                if timezone_data:

                                    logger.info(f"Scraped Time Zone Data: --> '{timezone_data[0]}'") if self.REGEX_LOGS else None
                                    data_process = fetch.removesuffix(timezone_data[0])
                                    if timezone_data[0] in self.TZ_EXCLUDE:
                                        logger.info("Timezone scraped found in Exclusion list. Deleting....") if self.REGEX_LOGS else None
                                        timezone_data = ''
                                    logger.info(f"Time Data without Timezone --> {data_process}") if self.REGEX_LOGS else None
                                else:
                                    logger.debug(f"No timezone data located on |{fetch}|...") if self.REGEX_LOGS else None
                            except ValueError as e:
                                logger.debug(f"Error |{e}|: No valid timezone to parse.. Skipping") if self.REGEX_LOGS else None

                        if not data_process:
                            data_process = fetch

                        clean_data = datetime.strptime(data_process,ptrn[0])

                        logger.info(f"Data after cleaning --> {clean_data}") if self.REGEX_LOGS else None

                        if timezone_data:
                            logger.info("\nAdding timezone to Clean Data appending...\n") if self.REGEX_LOGS else None
                            final_data_ls.append(clean_data.strftime(ptrn[1])+timezone_data[0])
                        else:
                            logger.info("\nClean Data appending...\n") if self.REGEX_LOGS else None
                            final_data_ls.append(clean_data.strftime(ptrn[1]))

                        # STOP PATTERN LOOP ONCE MATCHES
                        break

                    except ValueError as e:
                        logger.debug(f"Error |{e}|: strptime pattern not valid for current data.. Skipping") if self.REGEX_LOGS else None

        if final_data_ls:
            final_data = " - ".join(list(dict.fromkeys(final_data_ls)))
            logger.info(f"\nFinal Datetime Data: {final_data}")
        else:
            logger.info("\nNo valid datetime data to be cleaned...")
            if fetch_date:
                logger.debug(f"No valid data but REGEX was detected... Setting 'final_data' to <NO DATA|REGEX DETECTED>") if self.REGEX_LOGS else None
                final_data = f"<NO DATA|REGEX DETECTED>\n{fetch_date}" if self.NO_MATCH_REGEX_LOGS else ''

        return final_data

    def sort_startups(self,data):

        # CHECK IF DATA IS EMPTY
        if not data:
            logger.debug("Data is empty. Returning as False") if self.REGEX_LOGS else None
            return False, ''

        # Get Words Substring
        get_words = data.lower()

        # Get Words Whole
        whole_words_temp = data.lower().split(" ")
        # Remove Non-Alphanumeric Characters
        get_words_whole = [self.re.sub(r"[^a-zA-Z0-9]","",x) for x in whole_words_temp]

        logger.info(f"Sorted Words from the Data\n{get_words_whole}") if self.REGEX_LOGS else None
        logger.info(f"List of Words: {get_words_whole}") if self.REGEX_LOGS else None

        # remove case-sensitivity in WHOLE WORDS CRITERIA
        whole_words_criteria = [x.lower() for x in self.STARTUP_EVENT_KEYWORDS['WHOLE']]
        logger.info(f"WHOLE Words Criteria: {whole_words_criteria}") if self.REGEX_LOGS else None

        # ---------- PRIORITY KEYWORD CHECK -------------- #

        # Remove case sensitivity
        priority_words = [x.lower() for x in self.STARTUP_EVENT_KEYWORDS['PRIORITY']]
        logger.info(f"PRIORITY Words: {priority_words}") if self.REGEX_LOGS else None

        # for word in new_data:
        for word in priority_words:
            logger.debug(f"\nPRIORITY 'Word': {word}") if self.REGEX_LOGS else None
            # logger.debug(f"\nData: {word}") if self.REGEX_LOGS else None
            # if word in priority_words:
            if word.lower() in whole_words_criteria:
                logger.debug(f"\nPRIORITY Criteria: WHOLE") if self.REGEX_LOGS else None

                if word.lower() in get_words_whole:
                    logger.info("\nData found as Eligible Startup....\n")
                    return True, f'PRIORITY: {word}'
                else:
                    logger.info(f"Word {word} not found on Eligible Startup Events Criteria 'PRIORITY'...\n") if self.REGEX_LOGS else None

            else:
                logger.debug(f"\nPRIORITY Criteria: Substring") if self.REGEX_LOGS else None

                if word.lower() in get_words:
                    logger.info("\nData found as Eligible Startup....\n")
                    return True, f'PRIORITY: {word}'
                else:
                    logger.info(f"Word {word} not found on Eligible Startup Events Criteria 'PRIORITY'...\n") if self.REGEX_LOGS else None

        # --------- COMBINATION KEYWORD CHECK ------------ #

        comb_words_list = self.STARTUP_EVENT_KEYWORDS['COMBINATION']

        for comb_words in comb_words_list:

            # Remove case sensitivity
            comb_words = [x.lower() for x in comb_words]

            logger.debug(f"Combination: {comb_words}") if self.REGEX_LOGS else None
            logger.debug(f"Count: {len(comb_words)}") if self.REGEX_LOGS else None

            criteria_num = len(comb_words)
            criteria_pass = 0

            for word in comb_words:
                # if word in new_data:
                if word.lower() in whole_words_criteria:
                    logger.debug(f"\nCOMBINATION Criteria: WHOLE") if self.REGEX_LOGS else None

                    if word.lower() in get_words_whole:
                        criteria_pass+=1
                        logger.info(f"Word ->'{word}' passes Startup Event Criteria 'COMBINATION'...") if self.REGEX_LOGS else None
                        logger.info(f"Pass Count -> '{criteria_pass}'\n") if self.REGEX_LOGS else None

                        if criteria_pass >= criteria_num:
                            logger.info("\nData found as Eligible Startup....\n")
                            return True, f'COMBINATION: {comb_words}'

                    else:
                        logger.info(f"Word -> '{word}' not found on Eligible Startup Events Criteria 'COMBINATION'...\n") if self.REGEX_LOGS else None

                else:
                    logger.debug(f"\nCOMBINATION Criteria: Substring") if self.REGEX_LOGS else None
                    if word.lower() in get_words:
                        criteria_pass+=1
                        logger.info(f"Word ->'{word}' passes Startup Event Criteria 'COMBINATION'...") if self.REGEX_LOGS else None
                        logger.info(f"Pass Count -> '{criteria_pass}'\n") if self.REGEX_LOGS else None

                        if criteria_pass >= criteria_num:
                            logger.info("\nData found as Eligible Startup....\n")
                            return True, f'COMBINATION: {comb_words}'
                    else:
                        logger.info(f"Word -> '{word}' not found on Eligible Startup Events Criteria 'COMBINATION'...\n") if self.REGEX_LOGS else None


        logger.info("\nIneligible Startup Data...\n")
        return False, ''


    def get_startup_links(self,data):

        # CHECK IF DATA IS EMPTY
        if not data:
            logger.debug("Data is empty. Returning as Empty String") if self.REGEX_LOGS else None
            return ''

        link_regex = self.STARTUP_LINK_PATTERNS

        get_links = self.perform_regex(link_regex,data)

        sorted_links = ", ".join([x for x in get_links])

        return sorted_links


    def get_startup_name(self,data):

        # CHECK IF DATA IS EMPTY
        if not data:
            logger.debug("Data is empty. Returning as Empty String") if self.REGEX_LOGS else None
            return ''

        startup_names = self.STARTUP_NAMES
        final_data = ''
        startup_names_list = []

        logger.debug(f"STARTUP_NAMES: {startup_names}") if self.REGEX_LOGS else None

        # Get Words from Data
        get_data = data.lower()

        # Remove Non-Alphanumeric Characters
        # new_data = [self.re.sub(r"[^a-zA-Z0-9]","",x) for x in get_words]

        logger.info(f"Data to be checked:\n{get_data}") if self.REGEX_LOGS else None

        for name in startup_names:
            logger.debug(f"Checking Name: {name}") if self.REGEX_LOGS else None
            if name.lower() in get_data:
                logger.info("\nStartup Name located...\n")
                startup_names_list.append(name)
            else:
                logger.info("Startup Name cannot be found...")

        final_data = ", ".join([x for x in startup_names_list])

        return final_data

    def clean_date(self,data):

        date_criteria = self.DATE_PATTERNS
        date_regex = self.DATE_PATTERNS_RE

        # remove double spacing
        data = data.replace("  "," ")

        return self.perform_strptime(date_criteria,date_regex,data,'date')

    def clean_time(self,data):

        time_criteria = self.TIME_PATTERNS
        time_regex = self.TIME_PATTERNS_RE

        # remove double spacing
        data = data.replace("  "," ")

        return self.perform_strptime(time_criteria,time_regex,data,'time')

    def contact_info(self,data):
        """
        Takes a string and pulls all the phone numbers
        based on regex and format all of the numbers
        in a clean format
        :params: data -> str
        :return: str
        """
        phone_number_criteria = self.PHONE_NUMBER_PATTERNS
        email_criteria = self.EMAIL_PATTERNS

        clean_phone_numbers = list(set(self.perform_regex(phone_number_criteria,data)))
        clean_emails = list(set(self.perform_regex(email_criteria,data)))

        logger.debug(f"\nClean Phone Number(s) List: |{clean_phone_numbers}|\n")

        logger.info(f"Phone Number(s) --> {len(clean_phone_numbers)}")
        logger.info(f"Email(s) --> {len(clean_emails)}")

        sorted_phone_numbers = ", ".join([x for x in clean_phone_numbers])
        sorted_emails = ", ".join([x for x in clean_emails])

        if sorted_phone_numbers or sorted_emails:
            result = f"Phone Number(s):\n{sorted_phone_numbers}\nEmail(s):\n{sorted_emails}"
        else:
            result = ""

        return result


pipeline_re = RegExGGV()
