import scrapy
# from scrapy import Selector
from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usa0002Spider(scrapy.Spider):
    name = 'usa-0002'
    country = 'US'
    start_urls = ['https://www.eventbrite.com/o/w-p-carey-school-of-business-at-arizona-state-university-11043978456']
    
    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        
        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()
        
        self.driver.get("https://wpcarey.asu.edu/")

        logo = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')
        
        university_name = self.driver.find_element(By.XPATH,"//div[contains(@class, 'navbar-container')]/a").text
        
        self.driver.get('https://wpcarey.asu.edu/about/contact')
        
        university_contact_info = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"(//div[contains(@class,'panel-body')])[2]/div[1]")))).text 
        
        self.driver.get(response.url)
            
        EventLinks = WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located((By.XPATH,"(//div[contains(@class,'eds-show-up-mn organizer-profile__event-renderer__grid')])[1]//div[contains(@class,'eds-event-card--consumer')]//a[contains(@tabindex, '0')]")))

        for i in EventLinks:       
            self.getter.get(i.get_attribute('href'))
            
            RawEventName = (WebDriverWait(self.getter, 60).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class,'listing-hero-title')]")))).text
            
            print(RawEventName,"+"*100)
            RawEventDesc = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text structured-content__module l-align-left l-mar-vert-6 l-sm-mar-vert-4 text-body-medium')]").text
            
            try:
                RawEventDate = self.getter.find_element(By.XPATH,"//div[contains(@class,'js-date-time-first-line')]").text
            except:
                RawEventDate = None
                
            try:
                RawEventTime = self.getter.find_element(By.XPATH, "//div[contains(@class,'js-date-time-second-linet')]").text
            except:
                RawEventTime = None
            
            event_name.append(RawEventName)
            event_desc.append(RawEventDesc)
            event_date.append(RawEventDate)
            event_time.append(RawEventTime)

        for i in range(len(event_name)):
            data = ItemLoader(item = GgventuresItem(), selector = i)
            data.add_value('university_name',university_name)
            data.add_value('university_contact_info',university_contact_info)
            data.add_value('logo',logo)
            data.add_value('event_name', event_name[i])
            data.add_value('event_desc', event_desc[i])
            data.add_value('event_date', event_date[i])
            data.add_value('event_time', event_time[i])
            yield data.load_item()
        self.driver.quit()
        self.getter.quit()
            # data.add_value('logo',logo)
            # data.add_value('event_time',event_time)
            # data.add_value('event_link',event_link)
            # data.add_value('startups_name',startups_name)
            # data.add_value('startups_link',startups_link)
            # data.add_value('startups_contact_info',startups_contact_info)
