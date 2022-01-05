# from __future__ import print_function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import smtplib

import time, os, sys

from binaries import logger, SMTP_SERVER, SMTP_PORT, SMTP_EMAIL, SMTP_KEY

client_recipients = []
dev_recipients = ['goldengooseventures.developer@gmail.com', 'kingcobra1325@gmail.com','joachim.cobar@gmail.com']


def website_changed(spider="Default Spider", university_name="Default University"):
    try:
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

def unique_event(spider="Default Spider", university_name="Default University", href='default.link'):
    try:
        # EMAIL INIT
        for recipient in dev_recipients:
            with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
                mail.ehlo()
                mail.starttls()
                mail.login(SMTP_EMAIL,SMTP_KEY)

                msg = MIMEMultipart('alternative')
                msg['Subject'] = f'GGV BOT Unique Event - {spider}'
                msg['To'] = recipient
                msg['From'] = 'goldengooseventures.developer@gmail.com'

                # EMAIL CONTENT
                html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                 <head>
                  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                  <title>Unique Event Detected on {spider} - {university_name}</title>
                  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                </head>
                <body style="background-color:black;color:white">
                <h1 style="text-align:center;color:white">Unique Event - {university_name}</h1>
                <h4 style="color:white">The Spider: {spider} has found a Unique Event on the {university_name} website
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
                logger.debug(f'Unique Event Detected Email from {spider} successfully sent to {msg["To"]}')

    except Exception as e:
        logger.error("Exception when calling Email Bot->: %s\n" % e)

def missing_info_email(spider="Default Spider", university_name="Default University", missing_info=['missing','info'], web_link="www.google.com"):
    try:
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
                {unpack}
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
    try:
        # EMAIL INIT
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
