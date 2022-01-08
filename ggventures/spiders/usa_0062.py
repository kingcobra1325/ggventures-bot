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


class Usa0062Spider(scrapy.Spider):
    name = 'usa_0062'
    country = 'US'
    # allowed_domains = ['https://www.sju.edu/haub-school-business']
    start_urls = ['https://www.sju.edu/haub-school-business/']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:

            self.driver.get(response.url)

            logo = 'https://upload.wikimedia.org/wikipedia/commons/a/a5/HaubLogo.png'

            university_name = "Saint Joseph's University, Haub School of Business"

            university_contact_info = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'info-container')]"))).text

            self.driver.get('https://www.sju.edu/events?trumbaEmbed=filterview%3DHSB')

            # number_of_months = 3
            # #
            # for scrape_month in range(number_of_months):

                # try:
                    # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@id,'tribe-events-day')]/a")))
            # self.driver.switch_to.frame(WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@title,'List Calendar View')]"))))

            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'List Calendar View')]")))

            EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'twDescription')]/a")))

            for i in EventLinks:

                data = ItemLoader(item = GgventuresItem(), selector = i)

                link = i.get_attribute('href')
                self.getter.get(link)

                # if 'saunders.rit.edu/events' in self.getter.current_url:

                logger.info(f"Currently scraping --> {self.getter.current_url}")

                WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]")))

                # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail - Enhanced')]"))

                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                data.add_value('logo',logo)
                data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'twEDDescription')]"))).text)
                data.add_value('event_desc', self.getter.find_element(By.XPATH,"//table[contains(@class,'twEDContent')]").text)
                data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'twEDStartEndRange')]").text)
                data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'twEDStartEndRange')]").text)
                # try:
                #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
                # except NoSuchElementException as e:
                #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-range')]").text)
                data.add_value('event_link', link)


                yield data.load_item()

                self.getter.switch_to.default_content()
                # else:
                #     logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                #     unique_event(self.name,university_name,self.getter.current_url)
                #     logger.debug("Skipping............")

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
