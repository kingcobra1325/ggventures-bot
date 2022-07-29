import os,gc,smtplib
import pandas as pd

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from binaries import Google_Sheets, DEVELOPER_EMAILS, EMAIL_OFFLINE_COPY, SMTP_PORT, SMTP_EMAIL,SMTP_SERVER,SMTP_KEY
from spreadsheet import get_dataframe

from lib.baselogger import LoggerMixin

client_recipients = []
dev_recipients = DEVELOPER_EMAILS
email_copy_recipients = EMAIL_OFFLINE_COPY

next_line = '\n'

class EmailCopySheet(LoggerMixin):
    """
    Class that sends an Email offline copy of the
    spreadsheet to recepients
    """

    def __init__(self):
        self.logger.debug("Initializing sending Email copy of Spreadsheet...")
        self.spreadsheet = Google_Sheets()
    
    def download_offline_copy(self):
        filename = f"{datetime.utcnow().strftime('%Y-%m-%d')} GGVentures Offline Sheet.xlsx"
        self.logger.debug(f"Filename: {filename}")
        for i, worksheet in enumerate(self.spreadsheet.worksheets()):
            self.logger.debug(f"Index: {i} - Worksheet {worksheet.title}")
            self.logger.info(f"Writing {worksheet.title} into offline sheet file...")
            if i == 0:
                with pd.ExcelWriter(filename, engine="openpyxl", mode='w') as writer:
                    df = get_dataframe(worksheet.title,worksheet)
                    df.to_excel(writer, sheet_name=worksheet.title, index=False)
                    # Delete DataFrame / Free System Memory
                    del [df]
                    gc.collect()
            else:
                with pd.ExcelWriter(filename, engine="openpyxl", mode='a',if_sheet_exists='replace') as writer:
                    df = get_dataframe(worksheet.title,worksheet)
                    df.to_excel(writer, sheet_name=worksheet.title, index=False)
                    # Delete DataFrame / Free System Memory
                    del [df]
                    gc.collect()
        return filename


    def send_copy_via_email(self):
        try:
            filename = self.download_offline_copy()
            for recipient in email_copy_recipients:
                with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as mail:
                    mail.ehlo()
                    mail.starttls()
                    mail.login(SMTP_EMAIL,SMTP_KEY)

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = f"GGVentures Sheet Copy - {datetime.utcnow().strftime('%m-%d-%Y')}"
                    msg['To'] = recipient
                    msg['From'] = 'goldengooseventures.developer@gmail.com'

                    # EMAIL CONTENT
                    html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                    <title>GGVentures Sheet Copy</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                    </head>
                    <body style="background-color:black;color:white">
                    <h5 style="text-align:center">Timestamp: {datetime.utcnow().strftime('%m-%d-%Y %I:%M:%S %p')}</h5>
                    </body>
                    </html>"""
                    msg.attach(MIMEText(html,'html'))

                    # Attach Offline Copy to Email
                    with open(filename, "rb") as fil:
                        part = MIMEApplication(
                            fil.read(),
                            Name=filename
                        )
                    # After the file is closed
                    part['Content-Disposition'] = f'attachment; filename={filename}'
                    msg.attach(part)



                    mail.sendmail(msg['From'], msg['To'], msg.as_string())
                    self.logger.info(f'Email with Spreadsheet Copy successfully sent to {msg["To"]}')
            self.logger.debug(f"Deleting File {filename}...")
            os.remove(filename)
        except Exception as e:
            self.logger.error("Exception when calling Email Bot->: %s\n" % e)
