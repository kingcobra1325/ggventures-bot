import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Usa0013Spider(scrapy.Spider):
    name = 'usa_0013'
    country = 'US'
    start_urls = ['https://www.csulb.edu/']

    def __init__(self, response):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None
    
    def parse(self, response):
        try:
            self.driver.get(response.url)
            
            event_name = list()
            event_date = list()
            event_time = list()
            event_desc = list()

            #cannot find logo in website but it appears in fb
            # logo = (WebDriv   erWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'brand')]/a")))).value_of_css_property('background')
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]
            
            university_name = self.driver.find_element(By.XPATH , "//div[contains(@class,'content')]//img").get_attribute('alt')
            
            university_contact_info = self.driver.find_element(By.XPATH, "//div[contains(@class,'tel')]").text
            
            self.driver.get("http://specialevents.csulb.edu/mastercalendar/MasterCalendar.aspx")

            
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'items-scroller')]/div")))

            for i in EventLinks:
                i.click()
                
                EventPopUp = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'six columns scroller-text')]/h1")))
                
                EventPopUp.click()
                
                RawEventName = self.getter.find_element(By.XPATH,"//h1[contains(@class,'tribe-events-single-event-title')]").text
                
                RawEventDesc = self.getter.find_element(By.XPATH,"//div[starts-with(@class, 'tribe-events-single-event-description tribe-events-content')]/p[1]").text
                
                RawEventDate = self.getter.find_element(By.XPATH,"//abbr[contains(@class,'tribe-events-abbr tribe-events-start-date published dtstart')]").text
                
                RawEventTime = self.getter.find_element(By.XPATH,"//div[contains(@class,'tribe-events-abbr tribe-events-start-time published dtstart')]").text
                
                event_name.append(RawEventName)
                event_desc.append(RawEventDesc)
                event_date.append(RawEventDate)
                event_time.append(RawEventTime)

                newLink = self.driver.find_element(By.XPATH,"//a[contains(@rel, 'next')]").get_attribute('href')
                self.driver.get(newLink)
 

            for i in range(len(event_name)):
                data = ItemLoader(item = GgventuresItem(), selector = i)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                # data.add_value('logo',logo)
                data.add_value('event_name', event_name[i])
                data.add_value('event_desc', event_desc[i])
                data.add_value('event_date', event_date[i])
                data.add_value('event_time', event_time[i])
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
