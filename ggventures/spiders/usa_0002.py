import scrapy

from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0002Spider(scrapy.Spider):
    name = 'usa-0002'
    # allowed_domains = ['https://wpcarey.asu.edu/calendarofevents']
    start_urls = ['https://wpcarey.asu.edu/']

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        logolink = "https://wpcarey.asu.edu/calendarofevents"

        # options = webdriver.ChromeOptions()
        # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        # options.add_argument(f'user-agent={user_agent}')
        # options.add_argument('--headless')
        # options.add_argument('--log-level 3')
        # driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        # getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
        self.driver.get(logolink)
        height = self.driver.execute_script("return document.body.scrollHeight")


        logo = (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')

        self.driver.get('https://www.asu.edu/about/contact')

        university_contact_info = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'formatted-text')]/p[1]"))).text + WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'formatted-text')]/p[2]"))).text

        self.driver.get(response)

        for i in range(1,height,int(height/5)):
            self.driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)

        EventLinks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//h3/a")))

        university_name = self.driver.find_element(By.XPATH,"//div[contains(@class, 'navbar-container')]/a").text

        event_name = list()
        event_date = list()
        event_time = list()
        event_desc = list()

        for i in EventLinks:
            data = ItemLoader(item = GgventuresItem(), selector = i)
            self.getter.get(i.get_attribute('href'))
            RawEventName = (WebDriverWait(self.getter, 10).until(EC.presence_of_element_located((By.XPATH,"//div/h1")))).text
            event_name.append(RawEventName)

            RawEventDesc = self.getter.find_elements(By.XPATH,"//div[starts-with(@class, 'g-group')]")
            if len(RawEventDesc) == 0:
                RawEventDesc = self.getter.find_elements(By.XPATH,"//div[starts-with(@class, 'view-content')]/div/p")
            DescString = ''
            for x in RawEventDesc:
                DescString += x.text
            event_desc.append(DescString)

            RawEventDate = self.getter.find_element(By.XPATH,"//div[contains(@class,'view-content')]/div/p").text
            event_date.append(RawEventDate)

            RawEventTime = self.getter.find_element(By.XPATH, "//div[contains(@class,'view-content')]/div/p/br").text
            event_time.append(RawEventTime)

            data.add_value('university_name',university_name)
            data.add_value('university_contact_info',university_contact_info)
            data.add_value('logo',logo)
            data.add_value('event_time', RawEventTime)
            # data['event_link']
            # data['startups_name']
            # data['startups_link']
            # data['startups_contact_info']
            data.add_value('event_name', RawEventName)
            data.add_value('event_desc', DescString)
            data.add_value('event_date', RawEventDate)
            yield data.load_item()

        self.driver.quit()
        self.getter.quit()
        # for i in range(len(EventLinks)):
        #     print(university_name)
        #     print(university_contact_info)
        #     print(logo)
        #     print(event_name[i])
        #     print(event_desc[i])
        #     print(event_date[i])
        #     print(event_time[i])
