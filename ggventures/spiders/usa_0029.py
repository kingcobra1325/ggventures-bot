import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, website_changed

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Usa0029Spider(scrapy.Spider):
    name = 'usa_0029'
    country = 'US'
    start_urls = ["https://www.gabelliconnect.com/gabelli-london-speaker-series/"]

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

            self.driver.get("https://www.fordham.edu/gabelli-school-of-business/")

            logo = 'https://s3.amazonaws.com/campusreel-logos/colleges/college_images/000/002/941/medium/gabelli_logo.jpg?1607371510'

            university_name = self.driver.find_element(By.XPATH , "//title").get_attribute('textContent')

            self.driver.get("https://411.fordham.edu/?_ga=2.205200528.1053137397.1641397151-661834456.1641397151")

            university_contact_info = '\n'.join([x.text for x in WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class,'tel')]/parent::li")))])


            # GABELLI CONNECT

            self.driver.get(response.url)

            no_events = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//p[contains(text(),'no further upcoming events')]")))
            # no_events = self.driver.find_element(By.XPATH, "//li[contains(text(),'No upcoming')]")

            if not no_events:
                logger.debug('Changes to Events on current Spider. Sending emails....')
                website_changed(self.name,university_name)
            else:
                logger.debug('No changes to Events on current Spider. Skipping.....')

            # GABELLI CALENDAR

            self.driver.get('https://www.gabelliconnect.com/calendar/')

            number_of_months = 3
            #
            for scrape_month in range(number_of_months):

                try:
                    # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@id,'tribe-events-day')]/a")))

                    EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@id,'tribe-events-day')]")))

                    for i in EventLinks:

                        if i.find_elements(By.XPATH,"./following-sibling::div//a"):
                            link = i.find_element(By.XPATH,"./following-sibling::div//a").get_attribute('href')

                            data = ItemLoader(item = GgventuresItem(), selector = i)

                            self.getter.get(link)

                            logger.info(f"Currently scraping --> {self.getter.current_url}")

                            data.add_value('university_name',university_name)
                            data.add_value('university_contact_info',university_contact_info)
                            data.add_value('logo',logo)
                            data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h2"))).text)
                            data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'single-event')]").text)
                            data.add_value('event_date', self.getter.find_element(By.XPATH,"//dt[contains(text(),'Date')]/following-sibling::dd").text)
                            data.add_value('event_time', self.getter.find_element(By.XPATH,"//dt[contains(text(),'Time')]/following-sibling::dd").text)
                            data.add_value('event_link', link)


                            yield data.load_item()
                except TimeoutException as e:
                    logger.debug(f"No available events for this month : {e} ---> Skipping...........")

                WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@rel,'next')]"))).click()
                time.sleep(10)






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
