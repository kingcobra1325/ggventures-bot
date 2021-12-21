import scrapy
# from scrapy import Selector
from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usa0003Spider(scrapy.Spider):
    name = 'usa-0003'
    country = 'US'
    start_urls = ['https://calendar.auburn.edu/calendar']
    
    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        
        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()
        
        self.driver.get(response.url)

        logo = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'hidden-print')]")))).get_attribute('src')
        
        university_name = self.driver.find_element(By.XPATH,"//header/h1").get_attribute('textContent')
        
        university_contact_info = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'col-xs-6')]")))).text 
        
        EventLinks = WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'em-card_text')]/h3/a")))

        for i in EventLinks:       
            self.getter.get(i.get_attribute('href'))
            
            RawEventName = (WebDriverWait(self.getter, 60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'em-header-card_text')]/h1")))).text
            
            RawEventDesc = self.getter.find_element(By.XPATH,"//div[contains(@class,'em-content_about')]").text
            
            RawEventDate = self.getter.find_element(By.XPATH,"//p[contains(@class,'em-date')]").text 
            
            RawEventTime = self.getter.find_element(By.XPATH, "//p[contains(@class,'em-date')]").text
            
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
