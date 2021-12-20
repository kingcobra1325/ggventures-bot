import scrapy

from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0003Spider(scrapy.Spider):
    name = 'usa-0003'
    # allowed_domains = ['https://calendar.auburn.edu/calendar']
    start_urls = ['https://calendar.auburn.edu/calendar']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        self.driver.get(response)
        height = self.driver.execute_script("return document.body.scrollHeight")


        for i in range(1,height,int(height/5)):
            self.driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)

        EventLinks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'em-card_text')]/h3/a")))

        for i in EventLinks:
            data = ItemLoader(item = GgventuresItem(), selector = i)
            self.getter.get(i.get_attribute('href'))

            RawEventName = WebDriverWait(self.getter, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(@class, 'em-header-card_title')]")))
            RawEventDesc = WebDriverWait(self.getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'em-about_description')]/p")))
            RawEventLocation = WebDriverWait(self.getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'em-about_location')]/p")))
            RawEventDate = WebDriverWait(self.getter, 10).until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class, 'em-date')]")))

            # data.add_value('university_name',university_name)
            # data.add_value('university_contact_info',university_contact_info)
            # data.add_value('logo',logo)
            # data.add_value('event_time',event_time)
            # data.add_value('event_link',event_link)
            # data.add_value('startups_name',startups_name)
            # data.add_value('startups_link',startups_link)
            # data.add_value('startups_contact_info',startups_contact_info)
            data.add_value('event_name', RawEventName.text)
            data.add_value('event_desc', f"{RawEventDesc.text} {RawEventLocation.text}")
            data.add_value('event_date', RawEventDate.text)
            yield data.load_item()

            # print(RawEventName.text)
            # print(RawEventDesc.text)
            # print(RawEventLocation.text)
            # print(RawEventDate.text)

        self.getter.close()
        self.driver.close()
