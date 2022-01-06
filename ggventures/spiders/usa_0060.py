import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import re


class Usa0060Spider(scrapy.Spider):
    name = 'usa_0060'
    country = 'US'
    start_urls = ['https://saunders.rit.edu/contact']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:

            self.driver.get(response.url)

            logo = 'https://media-exp1.licdn.com/dms/image/C4D0BAQHzjEGARqOK2A/company-logo_200_200/0/1563224879458?e=2159024400&v=beta&t=e17m-hGu4F5isAP2o1YJJB8oqc1d3Q7dserLzxdlUp4'

            university_name = 'Rochester Institute of Technology, Saunders College of Business'

            university_contact_info = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'block-views')]"))).text

            self.driver.get('https://saunders.rit.edu/about/newsroom/events-calendar')

            # number_of_months = 3
            # #
            # for scrape_month in range(number_of_months):

                # try:
                    # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@id,'tribe-events-day')]/a")))

            EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'views-row')]//a")))

            for i in EventLinks:

                data = ItemLoader(item = GgventuresItem(), selector = i)

                link = i.get_attribute('href')
                self.getter.get(link)

                if 'saunders.rit.edu/events' in self.getter.current_url:

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@id,'page-title')]"))).text)
                    data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@property,'content')]").text)
                    try:
                        data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                        data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                        data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                    data.add_value('event_link', link)


                    yield data.load_item()
                else:
                    logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                    unique_event(self.name,university_name,self.getter.current_url)
                    logger.debug("Skipping............")

                # except TimeoutException as e:
                #     logger.debug(f"No available events for this month : {e} ---> Skipping...........")

                # WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@rel,'next')]"))).click()
                # time.sleep(10)






            # self.driver.get(response.url)
            #
            # EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='eventCard']")))
            #
            # for i in EventLinks:
            #
            #     RawEventName = (WebDriverWait(i,60).until(EC.presence_of_element_located((By.XPATH,".//h3")))).text
            #
            #     RawEventDesc = i.find_element(By.XPATH,".//span[@class='ng-binding']").text
            #
            #     RawEventDate = i.find_element(By.XPATH,".//div[contains(@class,'eventCard_date')]").text
            #
            #     try:
            #         RawEventTime = i.find_element(By.XPATH,".//div[contains(@class,'eventCard_date')]").text
            #     except:
            #         RawEventTime = None
            #
            #
            #     event_name.append(RawEventName)
            #     event_desc.append(RawEventDesc)
            #     event_date.append(RawEventDate)
            #     event_time.append(RawEventTime)
            #     event_link.append(i.get_attribute('href'))
            #


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
