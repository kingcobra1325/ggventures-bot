import scrapy

from binaries import Load_Driver, logger


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0002Spider(scrapy.Spider):
    name = 'usa-0002'
    country = 'US'
    allowed_domains = ['https://wpcarey.asu.edu/calendarofevents']
    start_urls = ['http://https://wpcarey.asu.edu//']
    
    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        logolink = "https://wpcarey.asu.edu/calendarofevents"
        
        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()
        
        self.driver.get(logolink)
        height = self.driver.execute_script("return document.body.scrollHeight")

        logo = tryXPATH(self.driver,False,True,"//img[contains(@class, 'vert')]",'src')
        # logo = (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')

        self.driver.get(response)

        for i in range(1,height,int(height/5)):
            self.driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)
            
        EventLinks = tryXPATH(self.driver,True,True,"//h3/a")
        # EventLinks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//h3/a")))


        for i in EventLinks:
            self.getter.get(i.get_attribute('href'))
            
            RawEventName = tryXPATH(self.getter,False,True,"//div/h1")
            # RawEventName = (WebDriverWait.driverWait(self.getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div/h1")))).text
            
            RawEventDesc = tryXPATH(self.getter,True,False,"//div[starts-with(@class, 'g-group')]")
            # RawEventDesc = self.getter.find_elements(By.XPATH,"//div[starts-with(@class, 'g-group')]")
            if len(RawEventDesc) == 0:
                RawEventDesc = tryXPATH(self.getter,True,False,"//div[starts-with(@class, 'view-content')]/div/p")
                # RawEventDesc = self.getter.find_elements(By.XPATH,"//div[starts-with(@class, 'view-content')]/div/p")
            DescString = ''
            for i in RawEventDesc:
                DescString += i.text
            
            RawEventDate = tryXPATH(self.getter,False,False,"//div[contains(@class,'view-content')]/div/p")
            # RawEventDate = self.getter.find_element(By.XPATH,"//div[contains(@class,'view-content')]/div/p").text   
            
            RawEventTime = tryXPATH(self.getter,False,False,"//div[contains(@class,'view-content')]/div/p/br")
            # RawEventTime = self.getter.find_element(By.XPATH, "//div[contains(@class,'view-content')]/div/p/br").text
            
            event_name.append(RawEventName)
            event_desc.append(DescString)
            event_date.append(RawEventDate)
            event_time.append(RawEventTime)

        university_name = tryXPATH(self.driver,False,False,"//div[contains(@class, 'navbar-container')]/a")
        # university_name = self.driver.find_element(By.XPATH,"//div[contains(@class, 'navbar-container')]/a").text

        self.driver.get('https://www.asu.edu/about/contact')

        university_contact_info = tryXPATH(self.driver,False,True,"//div[contains(@class, 'formatted-text')]/p[1]") + tryXPATH(self.getter,False,True,"//div[contains(@class, 'formatted-text')]/p[2]")
        # university_contact_info = WebDriverWait.driverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'formatted-text')]/p[1]"))).text + WebDriverWait.driverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'formatted-text')]/p[2]"))).text

        for i in range(len(event_name)):
            print(university_name)
            print(university_contact_info)
            print(logo)
            print(event_name[i])
            print(event_desc[i])
            print(event_date[i])
            print(event_time[i])
