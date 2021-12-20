import scrapy

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0003Spider(scrapy.Spider):
    name = 'usa-0003'
    country = 'US'
    allowed_domains = ['https://calendar.auburn.edu/calendar']
    start_urls = ['http://https://www.auburn.edu//']

    def parse(self, response):
        
        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()
        
        driver.get(link)
        height = driver.execute_script("return document.body.scrollHeight")

        logo = tryXPATH(driver,False,True,"//img[contains(@alt, 'Auburn University homepage') and contains(@class, 'hidden-print')]",'src')

        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)
            
        EventLinks = tryXPATH(driver,True,True,"//h3/a")

        for i in EventLinks:
            getter.get(i.get_attribute('href'))
            
            RawEventName = tryXPATH(getter,False,True,"//h1[contains(@class ,'em-header-card_title')]")
            
            RawEventDesc = tryXPATH(getter,False,False,"//div[starts-with(@class, 'em-content_about')]")
            
            RawEventDate = tryXPATH(getter,False,False,"//p[contains(@class, 'em-date')]")
            
            #Some Events have time embedded in Date
            #RawEventTime = tryXPATH(getter,False,False,"//div[contains(@class,'view-content')]/div/p/br")
            
            event_name.append(RawEventName)
            event_desc.append(RawEventDesc)
            event_date.append(RawEventDate)
            #event_time.append(RawEventTime)

        university_contact_info = tryXPATH(driver,False,True,"//div[contains(@class, 'col-xs-6')]")

        driver.get('https://www.auburn.edu/')

        university_name = tryXPATH(driver,False,True,"//title",'textContent')

        for i in range(len(EventLinks)):
            print(university_name)
            print(university_contact_info)
            print(logo)
            print(event_name[i])
            print(event_desc[i])
            print(event_date[i])
            #print(event_time[i])
