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
        driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver')
        driver.get(response)
        height = driver.get_window_size()['height']


        for i in range(1,height,int(height/3)):
            last_height = driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)


        RawEventName = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'events__title')]")))
        RawEventDesc = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'event__content')]/p")))
        RawEventDate = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'events-carousel__date')]")))

        EventName = list()
        EventDesc = list()
        EventDate = list()

        for i in range(len(RawEventName)):
            EventName.append(RawEventName[i].text)
            EventDesc.append(RawEventDesc[i].text)
            EventDate.append(RawEventDate[i].text.replace('\n',' '))

        for i in range(len(RawEventName)):
            print(EventDate[i])
            print(EventName[i])
            print(EventDesc[i])
