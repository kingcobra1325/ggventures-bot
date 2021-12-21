import scrapy
# from scrapy import Selector
from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0007Spider(scrapy.Spider):
    name = 'usa-0007'
    country = 'US'
    start_urls = ['https://events.bentley.edu/']
    
    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        self.driver.get(response.url)
        
        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()

        logo = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@id,'logo')]//img[contains(@alt, 'Bentley University')]")))).get_attribute('src')
        
        university_name = self.driver.find_element(By.XPATH , "//div[contains(@id,'logo')]//a[contains(@title,'Bentley University')]").get_attribute('title')

        university_contact_info = self.driver.find_element(By.XPATH,"//div[contains(@class,'footer-info')]").text

        EventLinks = self.driver.find_elements(By.XPATH, "//div/h3/a")
        for i in EventLinks:
            self.getter.get(i.get_attribute('href'))
                
            RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'box_content vevent grid_8')]/h1")))).text
            
            RawEventDesc = self.getter.find_element(By.XPATH,"//div[contains(@class,'description')]").text
            
            RawEventDate = self.getter.find_element(By.XPATH,"//p[contains(@class,'dateright')]").text
            
            RawEventTime = self.getter.find_element(By.XPATH,"//p[contains(@class,'dateright')]").text
            
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
