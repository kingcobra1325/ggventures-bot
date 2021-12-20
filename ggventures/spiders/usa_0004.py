import scrapy

from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usa0004Spider(scrapy.Spider):
    name = 'usa-0004'
    country = 'US'
    allowed_domains = ['https://www.babson.edu/about/news-events/babson-events/']
    start_urls = ['http://https://www.babson.edu//']
    
    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        driver.get(response)
        height = driver.execute_script("return document.body.scrollHeight")

        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()


        logo = None
        # logo draw
        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)
            

        for i in range(3):
            EventLinks = WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//li[contains(@class, 'event-item snippet event clearfix')]")))
            for o in EventLinks:
                event_name.append(o.find_element(By.XPATH,".//div[contains(@class, 'event-info')]/header").text.strip())
                event_desc.append(o.find_element(By.XPATH, ".//div[starts-with(@class, 'image')]").get_attribute('textContent').strip())
                event_date.append(o.find_element(By.XPATH, ".//div[contains(@class, 'event-date-box')]").text.strip())
                event_time.append(o.find_element(By.XPATH, "//p[contains(@class, 'categories_trigger ajax-load-link')]").text.strip())
            Next_Link = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 'next-search-link')]")))).get_attribute('href')
            driver.get(Next_Link)
            print(event_name)

        university_name = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH , "//div[contains(@class,'header__logo')]/a")))).get_attribute('title')

        university_contact_info = driver.find_element(By.XPATH,"//div[contains(@class, 'footer-addy')]/a[starts-with(@target, '_blank')]").text
            
        for i in range(len(event_name)):
            print(university_name)
            print(university_contact_info)
            print(logo)
            print(event_name[i])
            print(event_desc[i])
            print(event_date[i])
            print(event_time[i])
