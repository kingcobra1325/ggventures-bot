import scrapy

from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re



class Usa0006Spider(scrapy.Spider):
    name = 'usa-0006'
    country = 'US'
    allowed_domains = ['https://www.baylor.edu/business/news/index.php?id=86163']
    start_urls = ['http://https://www.baylor.edu/business//']
    
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

        logo = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class ,'logo')]"))).value_of_css_property('background')
        logo = re.findall(r'''\"(\S+)\"''',logo)[0]

        for i in range(1,height,int(height/5)):
            driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)
            
        Next_Link = driver.find_element(By.XPATH, "//input[contains(@type, 'submit')]")
        Next_Link.click()
            

        for i in range(1):
            EventLinks = driver.find_elements(By.XPATH, "//div[contains(@class, 'notResponsive')]//td[contains(@align, 'left')]/a")
            for i in EventLinks:
                i.click()
                print(len(driver.window_handles))
                new_window = driver.window_handles[2]
                driver.switch_to.window(new_window)
                event_name.append((WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@id, 'content')]/h1")))).text)
                event_desc.append(driver.find_element(By.XPATH, "//tr[3]").text)
                event_date.append(driver.find_element(By.XPATH, "//tr[1]/td[2]").text)
                #event_time.append(driver.find_element(By.XPATH, "//tr[1]/td[4]").text)
                #Some events don't have time and element position changes depends on the event
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            driver.get(driver.find_element(By.XPATH,"//div[contains(@class, 'box_title')]/a[3]").get_attribute('href'))

        university_name = driver.find_element(By.XPATH , "//a[contains(@class,'logo')]").get_attribute('textContent')

        driver.get("https://www.baylor.edu/business/index.php?id=87041")

        university_contact_info = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'two-columns')]")))).text
            
        for i in range(len(event_name)):
            print(university_name)
            print(university_contact_info)
            print(logo)
            print(event_name[i])
            print(event_desc[i])
            print(event_date[i])
            # print(event_time[i])
