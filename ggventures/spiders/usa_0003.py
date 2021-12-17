import scrapy

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0003Spider(scrapy.Spider):
    name = 'usa-0003'
    allowed_domains = ['https://calendar.auburn.edu/calendar']
    start_urls = ['http://https://www.auburn.edu//']

    def parse(self, response):
        options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')
        options.add_argument('--log-level 3') 
        driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        Getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        driver.get(response)
        height = driver.execute_script("return document.body.scrollHeight")


        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)

        EventLinks = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'em-card_text')]/h3/a")))

        for i in EventLinks:
            Getter.get(i.get_attribute('href'))
            
            RawEventName = WebDriverWait(Getter, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class, 'em-header-card_title')]")))
            RawEventDesc = WebDriverWait(Getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'em-about_description')]/p")))
            RawEventLocation = WebDriverWait(Getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'em-about_location')]/p")))
            RawEventDate = WebDriverWait(Getter, 10).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class, 'em-date')]")))

            print(RawEventName.text)
            print(RawEventDesc.text)
            print(RawEventLocation.text)
            print(RawEventDate.text)
            
        Getter.close()
        driver.close()
