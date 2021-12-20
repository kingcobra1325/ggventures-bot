import scrapy
# from scrapy import Selector
from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usa0004Spider(scrapy.Spider):
    name = 'usa-0004'
    country = 'US'
    start_urls = ['https://www.babson.edu/about/news-events/babson-events/']
    
    def __init__(self):
        self.driver = Load_Driver()

    def parse(self, response):
        
        height = self.driver.execute_script("return document.body.scrollHeight")

        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()
        
        self.driver.get(response.url)

        logo = None
        # logo draw
        
        university_name = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH , "//div[contains(@class,'header__logo')]/a")))).get_attribute('title')

        university_contact_info = self.driver.find_element(By.XPATH,"//div[contains(@class, 'footer-addy')]/a[starts-with(@target, '_blank')]").text
            

        for i in range(3):
            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//li[contains(@class, 'event-item snippet event clearfix')]")))
            for o in EventLinks:
                event_name.append(o.find_element(By.XPATH,".//div[contains(@class, 'event-info')]/header").text.strip())
                event_desc.append(o.find_element(By.XPATH, ".//div[starts-with(@class, 'image')]").get_attribute('textContent').strip())
                event_date.append(o.find_element(By.XPATH, ".//div[contains(@class, 'event-date-box')]").text.strip())
                event_time.append(o.find_element(By.XPATH, ".//p[contains(@class, 'categories_trigger ajax-load-link')]").text.strip())
            Next_Link = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 'next-search-link')]")))).get_attribute('href')
            self.driver.get(Next_Link)
            
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
        self.driver.quit()
        self.getter.quit()
            # data.add_value('logo',logo)
            # data.add_value('event_time',event_time)
            # data.add_value('event_link',event_link)
            # data.add_value('startups_name',startups_name)
            # data.add_value('startups_link',startups_link)
            # data.add_value('startups_contact_info',startups_contact_info)
