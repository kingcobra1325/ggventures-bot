import scrapy
# from scrapy import Selector
from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Usa0005Spider(scrapy.Spider):
    name = 'usa-0005'
    country = 'US'
    start_urls = ['https://zicklin.baruch.cuny.edu/events/']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        
    def parse(self, response):
        
        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()
        
        self.driver.get('https://zicklin.baruch.cuny.edu/')
        
        logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'zk-print-logo')]/img[contains(@id,'dtlogo')]")))).get_attribute('src')
        
        university_name = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//title")))).get_attribute('textContent')

        university_contact_info = self.driver.find_element(By.XPATH,"//a[contains(@class ,'phone')]").text
            
        
        self.driver.get(response.url)
        
        while True:
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'tribe-event-url news-listing-title')]")))

            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))
                
                RawEventName = self.getter.find_element(By.XPATH,"//h1[contains(@class,'tribe-events-single-event-title')]").text
                
                RawEventDesc = self.getter.find_element(By.XPATH,"//div[starts-with(@class, 'tribe-events-single-event-description tribe-events-content')]/p[1]").text
                
                RawEventDate = self.getter.find_element(By.XPATH,"//abbr[contains(@class,'tribe-events-abbr tribe-events-start-date published dtstart')]").text
                
                RawEventTime = self.getter.find_element(By.XPATH,"//div[contains(@class,'tribe-events-abbr tribe-events-start-time published dtstart')]").text
                
                event_name.append(RawEventName)
                event_desc.append(RawEventDesc)
                event_date.append(RawEventDate)
                event_time.append(RawEventTime)
            try:
                newLink = self.driver.find_element(By.XPATH,"//a[contains(@rel, 'next')]").get_attribute('href')
                self.driver.get(newLink)
            except NoSuchElementException:
                break 

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
