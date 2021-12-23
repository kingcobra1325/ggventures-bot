# from __future__ import print_function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import smtplib

import time, os, sys

from binaries import logger, SMTP_SERVER, SMTP_PORT, SMTP_EMAIL, SMTP_KEY


def missing_info_email(spider="Default Spider", university_name="Default University", missing_info=['missing','info'], web_link="www.google.com"):
    try:
        unpack = ''
        for x in missing_info:
            unpack = f"{unpack}<p>{x}</p>"

        # EMAIL INIT
        with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(SMTP_EMAIL,SMTP_KEY)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'GGV BOT Missing Information - {spider}'
            msg['To'] = 'goldengooseventures.developer@gmail.com'
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
            <h1 style="text-align:center">Missing Information - {university_name}</h1>
            <h4>The Spider: {spider} failed to scrape multiple information from {university_name}
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
        with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(SMTP_EMAIL,SMTP_KEY)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'GGV BOT ERROR - {spider}'
            msg['To'] = 'goldengooseventures.developer@gmail.com'
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
            <h1 style="text-align:center">Spider experienced an Error!</h1>
            <h4>The Spider: {spider} experienced an error while running
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
    # send_test_email()
    # error_email()
    # missing_info_email()
