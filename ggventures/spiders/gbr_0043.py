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

class Gbr0043Spider(scrapy.Spider):
    name = 'gbr_0043'
    country = 'United Kingdom'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://www.southampton.ac.uk/business-school/news/events/latest.page"]

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            self.driver.get("https://www.southampton.ac.uk/business-school/index.page")

            logo = "https://cdn.southampton.ac.uk/assets/site/design/images/uos-logo.svg"
            # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

            university_name = "University of Southampton,School of Management"
            
            # self.driver.get("https://www.sbs.ox.ac.uk/about-us/contact-us")
            
            # self.driver.find_element(By.XPATH,"//*[contains(text(),'General contacts')]").click()
            
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//dt[text()='Contact us']/..")))).text

            self.driver.get(response.url)    
            
            no_events = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//p[text()='There are no forthcoming events currently listed. Please see the archive for past events.']"))) 
            
            if not no_events:
                logger.debug('Changes to Events on current Spider. Sending emails....')
                website_changed(self.name,university_name)
            else:
                logger.debug('No changes to Events on current Spider. Skipping.....')  
            
            
            
            
        
            # counter = 0
            # EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='page-item-image-link']")))
            # for i in EventLinks:
            #     self.getter.get(i.get_attribute('href'))

            #     RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='hero-heading']")))).text

            #     try:
            #         RawEventDesc = self.getter.find_element(By.XPATH,"//article[starts-with(@class,'res-article-body')]").text
            #     except:
            #         RawEventDesc = None

            #     try:
            #         RawEventDate = self.getter.find_element(By.XPATH,"//time[@itemprop='startDate']").text
            #     except:
            #         RawEventDate = None
                    
            #     try:
            #         RawEventTime = None                    
            #         # RawEventTime = self.getter.find_element(By.XPATH,"//p[@class='article__meta__text']").text 
            #         # RawEventTime = RawEventDate
            #     except:
            #         RawEventTime = None
                    
            #     # try:
            #     #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//dt[text()='Contact']/..").text
            #     # except:
            #     #     RawStartContactInfo = None

            #     data = ItemLoader(item = GgventuresItem(), selector = counter)
            #     data.add_value('university_name',university_name)
            #     data.add_value('university_contact_info',university_contact_info)
            #     data.add_value('logo',logo)
            #     data.add_value('event_name', RawEventName)
            #     data.add_value('event_desc', RawEventDesc)
            #     data.add_value('event_date', RawEventDate)
            #     data.add_value('event_time', RawEventTime)
            #     data.add_value('event_link', i.get_attribute('href'))
            #     # data.add_value('startups_contact_info', RawStartContactInfo)
            #     counter+=1

            #     yield data.load_item()

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