import scrapy
import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0150Spider(scrapy.Spider):
    name = 'usa_0150'
    country = 'US'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://olin.wustl.edu/EN-US/Events/Pages/EventSearch.aspx"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://olin.wustl.edu/EN-US/Pages/default.aspx")

            logo = "https://olin.wustl.edu/sitecollectionimages/home_page/Olin_Business_School_logo.png"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "Washington University in Saint Louis,John M. Olin Business School"
            
            self.driver.get("https://olin.wustl.edu/EN-US/about-olin/Pages/Contact-Olin.aspx")
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@id='cstm-contentmain']")))).text

            self.driver.get(response.url)     
            
            counter = 0
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'events')]//a")))
            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                if 'https://events.olin.wustl.edu/' in self.getter.current_url:
                    EventNameXPATH = "//h1[contains(@class,'event-name')]"
                    EventDescXPATH = "//div[@id='description']"
                    EventDateXPATH = "//div[contains(@class,'event-date')]"                                
                elif 'https://wustl.force.com/' in self.getter.current_url:
                    EventNameXPATH = "//h1"
                    EventDescXPATH = "//div[@class='descrSection']/.."
                    EventDateXPATH = "(//div[contains(@class,'slds-text-title_bold')])[2]"

                RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,EventNameXPATH)))).text

                try:
                    RawEventDesc = self.getter.find_element(By.XPATH,EventDescXPATH).text
                except:
                    RawEventDesc = None

                RawEventDate = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,EventDateXPATH)))).text 

                try:
                    RawEventTime = RawEventDate
                except:
                    RawEventTime = None
                    
                # try:
                #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//dt[@class='custom-field-contact']/..").text
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