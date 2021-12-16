import scrapy

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0001Spider(scrapy.Spider):
    name = 'usa-0001'
    allowed_domains = ['https://kogod.american.edu/events?hsLang=en']
    start_urls = ['http://https://kogod.american.edu//']

    def parse(self, response):
        options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')
        options.add_argument('--log-level 3') 
        driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        driver.get(response)
        height = driver.execute_script("return document.body.scrollHeight")


        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)


        RawEventName = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'events__title')]")))
        RawEventDesc = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'event__content')]/p")))
        RawEventDate = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//article//div[contains(@class, 'events-carousel__date')]")))

        EventName = list()
        EventDesc = list()
        EventDate = list()

        for i in range(len(RawEventName)):
            EventName.append(RawEventName[i].text)
            EventDesc.append(RawEventDesc[i].text)
            EventDate.append(RawEventDate[i].text.replace('\n',' '))
