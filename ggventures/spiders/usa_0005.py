import scrapy

from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usa0005Spider(scrapy.Spider):
    name = 'usa-0005'
    allowed_domains = ['https://zicklin.baruch.cuny.edu/']
    start_urls = ['http://https://zicklin.baruch.cuny.edu//']

    def parse(self, response):
        driver.get(link)
        height = driver.execute_script("return document.body.scrollHeight")


        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)
            
        logo = tryXPATH(driver,False,True,"//div[contains(@class,'zk-print-logo')]/img[contains(@id,'dtlogo')]",'src')

        driver.get("https://zicklin.baruch.cuny.edu/events/")

        while True:
            EventLinks = tryXPATH(driver,True,True,"//a[contains(@class,'tribe-event-url news-listing-title')]")

            for i in EventLinks:
                getter.get(i.get_attribute('href'))
                
                RawEventName = tryXPATH(getter,False,True,"//h1[contains(@class,'tribe-events-single-event-title')]")
                
                RawEventDesc = tryXPATH(getter,False,False,"//div[starts-with(@class, 'tribe-events-single-event-description tribe-events-content')]/p[1]")
                
                RawEventDate = tryXPATH(getter,False,False,"//abbr[contains(@class,'tribe-events-abbr tribe-events-start-date published dtstart')]")
                
                RawEventTime = tryXPATH(getter,False,False,"//div[contains(@class,'tribe-events-abbr tribe-events-start-time published dtstart')]")
                
                event_name.append(RawEventName)
                event_desc.append(RawEventDesc)
                event_date.append(RawEventDate)
                event_time.append(RawEventTime)

            newLink = tryXPATH(driver,False,True,"//a[contains(@rel, 'next')]",'href')
            if newLink == '':
                break
            else:
                driver.get(newLink)

                
        driver.get('https://zicklin.baruch.cuny.edu/')
                
        university_name = tryXPATH(driver,False,True,"//title",'textContent')

        university_contact_info = tryXPATH(driver,False,False,"//a[contains(@class ,'phone')]")

        for i in range(len(event_name)):
            print(university_name)
            print(university_contact_info)
            print(logo)
            print(event_name[i])
            print(event_desc[i])
            print(event_date[i])
            print(event_time[i])
