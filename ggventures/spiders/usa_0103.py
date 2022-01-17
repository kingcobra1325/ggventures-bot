import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email,unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

class Usa0103Spider(scrapy.Spider):
    name = 'usa_0103'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://gsm.ucdavis.edu/calendar"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            event_name = list()
            event_date = list()
            event_time = list()
            event_desc = list()
            event_link = list()

            self.driver.get("https://gsm.ucdavis.edu/")

            logo = "https://mms.businesswire.com/media/20190508005251/en/720490/23/GSM_Stacked_300px.jpg"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of California - Davis,Graduate School of Management"
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class,'footer-contact')]")))).text

            self.driver.get(response.url)

            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='redirect']")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                
                if 'https://gsm.ucdavis.edu/event/' in self.getter.current_url:

                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='title']")))).text

                    try:
                        RawEventDesc = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='node-content']")))).text
                    except:
                        RawEventDesc = None

                    RawEventDate = self.getter.find_element(By.XPATH,"//ul[@class='node-event-dates']").text

                    try:
                        RawEventTime = RawEventDate
                    except:
                        RawEventTime = None


                    event_name.append(RawEventName)
                    event_desc.append(RawEventDesc)
                    event_date.append(RawEventDate)
                    event_time.append(RawEventTime)
                    event_link.append(i.get_attribute('href'))
                else:
                    logger.debug(f"Link: {i.get_attribute('href')} is a Unique Event. Sending Emails.....")
                    unique_event(self.name,university_name,i.get_attribute('href'))
                    logger.debug("Skipping............")
                    

            for i in range(len(event_name)):
                data = ItemLoader(item = GgventuresItem(), selector = i)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                data.add_value('logo',logo)
                data.add_value('event_name', event_name[i])
                data.add_value('event_desc', event_desc[i])
                data.add_value('event_date', event_date[i])
                data.add_value('event_time', event_time[i])
                data.add_value('event_link', event_link[i])

                yield data.load_item()

        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
    def closed(self, reason):
        try:
            self.driver.quit()
            self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
