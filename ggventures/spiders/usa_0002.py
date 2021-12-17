import scrapy

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0002Spider(scrapy.Spider):
    name = 'usa-0002'
    allowed_domains = ['https://wpcarey.asu.edu/calendarofevents']
    start_urls = ['http://https://wpcarey.asu.edu//']

    def parse(self, response):
        logolink = "https://wpcarey.asu.edu/calendarofevents"
        
        options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')
        options.add_argument('--log-level 3') 
        driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        driver.get(logolink)
        height = driver.execute_script("return document.body.scrollHeight")


        logo = (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')

        driver.get(response)

        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)
            
        EventLinks = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//h3/a")))

        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()

        for i in EventLinks:
            getter.get(i.get_attribute('href'))
            RawEventName = (WebDriverWait(getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div/h1")))).text
            event_name.append(RawEventName)
            
            RawEventDesc = getter.find_elements(By.XPATH,"//div[starts-with(@class, 'g-group')]")
            if len(RawEventDesc) == 0:
                RawEventDesc = getter.find_elements(By.XPATH,"//div[starts-with(@class, 'view-content')]/div/p")
            DescString = ''
            for i in RawEventDesc:
                DescString += i.text
            event_desc.append(DescString)
            
            RawEventDate = getter.find_element(By.XPATH,"//div[contains(@class,'view-content')]/div/p").text
            event_date.append(RawEventDate)
            
            RawEventTime = getter.find_element(By.XPATH, "//div[contains(@class,'view-content')]/div/p/br").text
            event_time.append(RawEventTime)

        university_name = driver.find_element(By.XPATH,"//div[contains(@class, 'navbar-container')]/a").text

        driver.get('https://www.asu.edu/about/contact')

        university_contact_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'formatted-text')]/p[1]"))).text + WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'formatted-text')]/p[2]"))).text


        for i in range(len(EventLinks)):
            print(university_name)
            print(university_contact_info)
            print(logo)
            print(event_name[i])
            print(event_desc[i])
            print(event_date[i])
            print(event_time[i])
