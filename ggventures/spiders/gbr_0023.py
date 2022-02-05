import scrapy
import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email,unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Gbr0023Spider(scrapy.Spider):
    name = 'gbr_0023'
    country = 'United Kingdom'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://www.northumbria.ac.uk/about-us/news-events/events/"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://www.northumbria.ac.uk/about-us/academic-departments/newcastle-business-school/")

            logo = "https://www.northumbria.ac.uk/-/media/40f0efdb3a6745fda5b0d982d53b8cd9.ashx"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "Northumbria University,Newcastle Business School"

            self.driver.get("https://www.northumbria.ac.uk/about-us/academic-departments/newcastle-business-school/contact-us/")

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='rich-text']")))).text

            self.driver.get(response.url)

            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//article[@class='rich-text']//a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                if 'https://www.northumbria.ac.uk/about-us/' in self.getter.current_url:

                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//header[@class='course-heading']")))).text

                    try:
                        RawEventDesc = self.getter.find_element(By.XPATH,"//div[@class='rich-text']").text
                    except:
                        RawEventDesc = None

                    try:
                        RawEventDate = self.getter.find_element(By.XPATH,"//div[@class='calendar']").text
                    except:
                        RawEventDate = None

                    try:
                        # RawEventTime = None
                        RawEventTime = self.getter.find_element(By.XPATH,"//p[@class='time']").text
                        # RawEventTime = RawEventDate
                    except:
                        RawEventTime = None

                    # try:
                    #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//section[contains(@class,'contact')]").text
                    # except:
                    #     RawStartContactInfo = None

                    data = ItemLoader(item = GgventuresItem(), selector = counter)
                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    data.add_value('event_name', RawEventName)
                    data.add_value('event_desc', RawEventDesc)
                    data.add_value('event_date', RawEventDate)
                    data.add_value('event_time', RawEventTime)
                    data.add_value('event_link', i.get_attribute('href'))
                    # data.add_value('startups_contact_info', RawStartContactInfo)


                    yield data.load_item()
                else:
                    logger.debug(f"Link: {i.get_attribute('href')} is a Unique Event. Sending Emails.....")
                    unique_event(self,university_name,self.getter.current_url,university_contact_info,logo)
                    logger.debug("Skipping............")

                counter+=1


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
