# from __future__ import print_function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import smtplib

from datetime import datetime, timezone
import time, os, sys, csv, gc

from binaries import logger, SMTP_SERVER, SMTP_PORT, SMTP_EMAIL, SMTP_KEY, DEVELOPER_EMAILS, GGV_SETTINGS, EMAIL_OFFLINE_COPY

from spreadsheet import Read_DataFrame_From_Sheet, Add_Event

from models import pipeline_re

from lib.error_dashboard import ErrorDashboard

client_recipients = []
dev_recipients = DEVELOPER_EMAILS
email_copy_recipients = EMAIL_OFFLINE_COPY

next_line = '\n'


"""
    Attempts to read a worksheet from the spreadsheet based on
    the 'Name'. If the worksheet doesn't exist, the worksheet is 
    going to be created. Gets the DataFrame from the Worksheet and
    returns both objects
    :params: Name -> Name of the Worksheet | spreadsheet -> Default: SPREADSHEET_MAIN 
    :return: df -> Pandas DataFrame | worksheet -> Worksheet Object from GSpread API
    """

def website_changed(spider="Default Spider", university_name="Default University"):
    """
    Attempts to read a worksheet from the spreadsheet based on
    the 'Name'. If the worksheet doesn't exist, the worksheet is 
    going to be created. Gets the DataFrame from the Worksheet and
    returns both objects
    :params: Name -> Name of the Worksheet | spreadsheet -> Default: SPREADSHEET_MAIN 
    :return: df -> Pandas DataFrame | worksheet -> Worksheet Object from GSpread API
    """
    try:
        # ------- LOG WEBSITE CHANGED TO ERRORS SHEETS -------#
        error_dashboard = ErrorDashboard()
        error_dashboard.log_error({
                                "Time" : datetime.utcnow(),
                                "Error" : f"Website EVENT Changed - {university_name}",
                                "SpiderName" : spider,
                                "Status" : ''
                })
        del error_dashboard
        gc.collect()

        # EMAIL INIT
        for recipient in dev_recipients:
            with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
                mail.ehlo()
                mail.starttls()
                mail.login(SMTP_EMAIL,SMTP_KEY)

                msg = MIMEMultipart('alternative')
                msg['Subject'] = f'GGV BOT Website Changes - {spider}'
                msg['To'] = recipient
                msg['From'] = 'goldengooseventures.developer@gmail.com'

                # EMAIL CONTENT
                html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                 <head>
                  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                  <title>Website Changes on {spider} - {university_name}</title>
                  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                </head>
                <body style="background-color:black;color:white">
                <h1 style="text-align:center;color:white">Website Changes - {university_name}</h1>
                <h4 style="color:white">The Spider: {spider} has detected changes from the {university_name} website
                <br>
                <p>Please check the website and contact the developers to modify the Spider code as soon as possible!</p>
                <br>
                </h4>
                <h5 style="text-align:center">Email Timestamp: {datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p')}</h5>
                </body>
                </html>"""

                msg.attach(MIMEText(html,'html'))

                mail.sendmail(msg['From'], msg['To'], msg.as_string())
                logger.debug(f'Website Changed Email from {spider} successfully sent to {msg["To"]}')

    except Exception as e:
        logger.error("Exception when calling Email Bot->: %s\n" % e)
        
def file_event(spider="No-Spider-Name", university_name="No-University-Name", href='No-Link', contact_info = 'No-Contact-Info', logo='NO-LOGO'):
    """
    Registers the event based on the parameters into the Spreadsheet
    and sends an email that a File Event is detected from the events
    """
    try:
        # ------- LOG FILE EVENTS TO MAIN SHEETS -------#
        # GET COUNTRY DF
        df, worksheet = Read_DataFrame_From_Sheet(spider.country)

        if GGV_SETTINGS.CLEAN_DATA_PIPELINE:
            logger.info("CLEANING 'university_contact_info'")
            logger.info(f"Processing --> {contact_info}")
            contact_info = pipeline_re.contact_info(data=str(contact_info))
            logger.info(f"Result --> {contact_info}")

        data = {
                    "Last Updated" : datetime.utcnow(),
                    "Event Name" : f'<FILE EVENT - {href}>',
                    "Event Date" : f'<FILE EVENT - {href}>',
                    "Event Time" : f'<FILE EVENT - {href}>',
                    "Event Link" : href,
                    "Event Description" : f'<FILE EVENT - {href}>',
                    "Startup Name(s)" : f'<FILE EVENT - {href}>',
                    "Startup Link(s)" : f'<FILE EVENT - {href}>',
                    "Startup Contact Info(s)" : f'<FILE EVENT - {href}>',
                    "University Name" : university_name,
                    "University Contact Info" : contact_info,
                    "Logo" : logo,
                    "SpiderName" : spider.name
        }

        # ADD ITEM TO DF
        Add_Event(data=data,country_df=df,country_worksheet=worksheet,country=spider.country)

        logger.info("Added FILE Event into Google Sheets....")

    except Exception as e:
        logger.error("Exception when calling Email Bot->: %s\n" % e)


def unique_event(spider="No-Spider-Name", university_name="No-University-Name", href='No-Link', contact_info = 'No-Contact-Info', logo='NO-LOGO'):
    """
    Registers the event based on the parameters into the Spreadsheet
    and sends an email that a Unique Event is detected from the events
    """
    try:
        # ------- LOG UNIQUE EVENTS TO MAIN SHEETS -------#
        # GET COUNTRY DF
        df, worksheet = Read_DataFrame_From_Sheet(spider.country)

        if GGV_SETTINGS.CLEAN_DATA_PIPELINE:
            logger.info("CLEANING 'university_contact_info'")
            logger.info(f"Processing --> {contact_info}")
            contact_info = pipeline_re.contact_info(data=str(contact_info))
            logger.info(f"Result --> {contact_info}")

        data = {
                    "Last Updated" : datetime.utcnow(),
                    "Event Name" : f'<UNIQUE EVENT - {href}>',
                    "Event Date" : f'<UNIQUE EVENT - {href}>',
                    "Event Time" : f'<UNIQUE EVENT - {href}>',
                    "Event Link" : href,
                    "Event Description" : f'<UNIQUE EVENT - {href}>',
                    "Startup Name(s)" : f'<UNIQUE EVENT - {href}>',
                    "Startup Link(s)" : f'<UNIQUE EVENT - {href}>',
                    "Startup Contact Info(s)" : f'<UNIQUE EVENT - {href}>',
                    "University Name" : university_name,
                    "University Contact Info" : contact_info,
                    "Logo" : logo,
                    "SpiderName" : spider.name
        }

        # ADD ITEM TO DF
        Add_Event(data=data,country_df=df,country_worksheet=worksheet,country=spider.country)

        logger.info("Added Unique Event into Google Sheets....")

        if GGV_SETTINGS.UNIQUE_EVENT_EMAILS:

            # ------- LOG UNIQUE EVENTS TO ERRORS SHEETS -------#
            # error_dashboard.log_error({
            #                         "Time" : datetime.utcnow(),
            #                         "Error" : f"Unique Event - {university_name}\n{href}",
            #                         "SpiderName" : spider.name,
            #                         "Status" : ''
            #         })

            # EMAIL INIT
            logger.info("Unique Events Email Enabled.... Sending..")
            for recipient in dev_recipients:
                with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
                    mail.ehlo()
                    mail.starttls()
                    mail.login(SMTP_EMAIL,SMTP_KEY)

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = f'GGV BOT Unique Event - {spider.name}'
                    msg['To'] = recipient
                    msg['From'] = 'goldengooseventures.developer@gmail.com'

                    # EMAIL CONTENT
                    html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml">
                     <head>
                      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                      <title>Unique Event Detected on {spider.name} - {university_name}</title>
                      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                    </head>
                    <body style="background-color:black;color:white">
                    <h1 style="text-align:center;color:white">Unique Event - {university_name}</h1>
                    <h4 style="color:white">The Spider: {spider.name} has found a Unique Event on the {university_name} website
                    <br>
                    <p>Please check the link of the Event for more details</p>
                    <p>Link: {href}</p>
                    <br>
                    </h4>
                    <h5 style="text-align:center">Email Timestamp: {datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p')}</h5>
                    </body>
                    </html>"""

                    msg.attach(MIMEText(html,'html'))

                    mail.sendmail(msg['From'], msg['To'], msg.as_string())
                    logger.debug(f'Unique Event Detected Email from {spider.name} successfully sent to {msg["To"]}')

    except Exception as e:
        logger.error("Exception when calling Email Bot->: %s\n" % e)

def missing_info_email(spider="Default Spider", university_name="Default University", missing_info=['missing','info'], web_link="www.google.com"):
    try:
        # ------- LOG ERRORS TO ERRORS SHEETS -------#
        error_dashboard = ErrorDashboard()
        error_dashboard.log_error({
                                "Time" : datetime.utcnow(),
                                "Error" : f"Missing Information - {university_name}:\n{next_line.join(missing_info)}\n{web_link}",
                                "SpiderName" : spider,
                                "Status" : ''
                })
        # EMAIL INIT
        for recipient in dev_recipients:
            with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
                mail.ehlo()
                mail.starttls()
                mail.login(SMTP_EMAIL,SMTP_KEY)

                msg = MIMEMultipart('alternative')
                msg['Subject'] = f'GGV BOT Missing Information - {spider}'
                msg['To'] = recipient
                msg['From'] = 'goldengooseventures.developer@gmail.com'

                # EMAIL CONTENT
                html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                 <head>
                  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                  <title>Missing Information from {spider} - {university_name}</title>
                  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                </head>
                <body style="background-color:black;color:white">
                <h1 style="text-align:center;color:white">Missing Information - {university_name}</h1>
                <h4 style="color:white">The Spider: {spider} failed to scrape multiple information from {university_name}
                <p>Missing Information: </p>
                <br>
                <p>Please check if all the information scraped are correct</p>
                <p>Link: {web_link}</p>
                <br>
                </h4>
                <h5 style="text-align:center">Email Timestamp: {datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p')}</h5>
                </body>
                </html>"""

                msg.attach(MIMEText(html,'html'))

                mail.sendmail(msg['From'], msg['To'], msg.as_string())
                logger.error(f'Missing Information Email from {spider} successfully sent to {msg["To"]}')

    except Exception as e:
        logger.error("Exception when calling Email Bot->: %s\n" % e)

def error_email(spider="Default Spider",error="Default Error"):
    """
    Sends an email when an Exception is called
    It shows the spider name - error and the traceback
    detail
    """
    try:
        # ------- LOG ERRORS TO ERRORS SHEETS -------#
        error_dashboard = ErrorDashboard()
        error_dashboard.log_error({
                                "Time" : datetime.utcnow(),
                                "Error" : f"ERROR:\n{error}",
                                "SpiderName" : spider,
                                "Status" : ''
                })
        del error_dashboard
        gc.collect()

        # EMAIL INIT
        if GGV_SETTINGS.SEND_EMAILS_PER_ERROR:
            for recipient in dev_recipients:
                with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
                    mail.ehlo()
                    mail.starttls()
                    mail.login(SMTP_EMAIL,SMTP_KEY)

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = f'GGV BOT ERROR - {spider}'
                    msg['To'] = recipient
                    msg['From'] = 'goldengooseventures.developer@gmail.com'

                    # EMAIL CONTENT
                    html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml">
                        <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                        <title>GGV BOT ERROR - {spider}</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                    </head>
                    <body style="background-color:black;color:white">
                    <h1 style="text-align:center;color:white">Spider experienced an Error!</h1>
                    <h4 style="color:white">The Spider: {spider} experienced an error while running
                    <p>Error Details: </p>
                    {error}
                    <br>
                    <p>Please check the code as soon as possible to address the issue as soon as possible!</p>
                    <br>
                    </h4>
                    <h5 style="text-align:center">Error Timestamp: {datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p')}</h5>
                    </body>
                    </html>"""

                    msg.attach(MIMEText(html,'html'))

                    mail.sendmail(msg['From'], msg['To'], msg.as_string())
                    logger.error(f'Error Email from {spider} successfully sent to {msg["To"]}')

    except Exception as e:
        logger.error("Exception when calling Email Bot->: %s\n" % e)

# if __name__ == '__main__':
#     unique_event()
    # send_test_email()
    # error_email()
    # missing_info_email()
    # website_changed()
