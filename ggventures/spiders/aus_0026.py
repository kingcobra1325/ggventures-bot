import scrapy
import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email,website_changed,unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Aus0026Spider(scrapy.Spider):
    name = 'aus_0026'
    country = 'Australia'
    # allowed_domains = ['https://bond.edu.au/intl/about-bond/academia/bond-business-school']
    start_urls = ["https://business.uq.edu.au/events"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://business.uq.edu.au/")

            logo = "https://images.squarespace-cdn.com/content/v1/5bb947c88d97400df83137ac/1585011292636-9EI1CGQ7GA7Q5IMQPXKE/BusinessSchool-SponsSmall-col-rgb.png?format=1000w"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Queensland,UQ Business School (Brisbane Graduate School of Business)"
            
            self.driver.get("https://business.uq.edu.au/contact")
            
            # self.driver.find_element(By.XPATH,"//*[contains(text(),'General contacts')]").click()
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='field-items']")))).text

            self.driver.get(response.url)     
        
            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='qt-event_tabs-foundation-tabs-1']//h3[@Class='event-session__title']/a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                
                if 'https://business.uq.edu.au/event/' in self.getter.current_url:

                    RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='panel-pane__content']")))).text

                    try:
                        RawEventDesc = self.getter.find_element(By.XPATH,"(//div[@class='row']/div[starts-with(@class,'layout-region__main')])[2]").text
                    except:
                        RawEventDesc = None

                    try:
                        RawEventDate = self.getter.find_element(By.XPATH,"//span[@class='date--start']/..").text
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
                    counter+=1

                    yield data.load_item()
                else:
                    logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
                    unique_event(self,university_name,self.getter.current_url,university_contact_info,logo)
                    logger.debug("Skipping............")

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
