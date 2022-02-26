import scrapy
import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email,website_changed

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Aus0027Spider(scrapy.Spider):
    name = 'aus_0027'
    country = 'Australia'
    # allowed_domains = ['https://bond.edu.au/intl/about-bond/academia/bond-business-school']
    start_urls = ["https://usq.edu.au/events"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://usq.edu.au/bela/school-of-business")

            logo = "https://usq.edu.au/Content/USQ/Charlie/Images/usq-logo.png"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Southern Queensland,Faculty of Business"
            
            self.driver.get("https://usq.edu.au/contact")
            
            # self.driver.find_element(By.XPATH,"//*[contains(text(),'General contacts')]").click()
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//span[text()='General Enquiries']/../../../..")))).get_attribute('textContent')

            self.driver.get(response.url)     
        
            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='c-event-preview']")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div/h1")))).text

                try:
                    RawEventDesc = self.getter.find_element(By.XPATH,"//div[@class='container']//div[starts-with(@class,'page-content')]").text
                except:
                    RawEventDesc = None

                try:
                    RawEventDate = self.getter.find_element(By.XPATH,"//div[@class='o-event-info__group-content']").text
                except:
                    RawEventDate = None
                    
                try:
                    # RawEventTime = None                    
                    # RawEventTime = self.getter.find_element(By.XPATH,"//span[@class='lw_start_time']").text 
                    RawEventTime = RawEventDate
                except:
                    RawEventTime = None
                    
                # try:
                #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//h4[text()=' Enquiry']/../..").text
                # except:
                #     RawStartContactInfo = None
                
                try:
                    RawEventStartupLink = self.getter.find_element(By.XPATH,"//a[text()='Attend via Zoom']").get_attribute('href')
                except:
                    RawEventStartupLink = None

                data = ItemLoader(item = GgventuresItem(), selector = counter)
                data.add_value('university_name',university_name)
                data.add_value('university_contact_info',university_contact_info)
                data.add_value('logo',logo)
                data.add_value('event_name', RawEventName)
                data.add_value('event_desc', RawEventDesc)
                data.add_value('event_date', RawEventDate)
                data.add_value('event_time', RawEventTime)
                data.add_value('event_link', i.get_attribute('href'))
                data.add_value('startups_link', RawEventStartupLink)
                # data.add_value('startups_contact_info', RawStartContactInfo)
                counter+=1

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
