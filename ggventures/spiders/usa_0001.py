import scrapy
# from scrapy import Selector
from time import sleep

from binaries import Load_Driver, logger

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0001Spider(scrapy.Spider):
    name = 'usa-0001'
    index = 0
    country = 'US'
    # allowed_domains = ['https://kogod.american.edu/']
    start_urls = ['https://kogod.american.edu/events?hsLang=en']


    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()

    def parse(self, response):
        self.driver.get(response.url)
        height = self.driver.execute_script("return document.body.scrollHeight")

        for i in range(1,height,int(height/5)):
            self.driver.execute_script("window.scrollBy(0, {0});".format(i))
            sleep(0.5)

        logo = (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@alt, 'American University Homepage')]")))).get_attribute('src')

        RawEventName = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'events__title')]")))
        RawEventDesc = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'event__content')]/p")))
        RawEventDate = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//article//div[contains(@class, 'events-carousel__date')]")))


        university_name = self.driver.find_element(By.XPATH,"//div[contains(@class, 'header__main')]/a").text
        university_contact_info = self.driver.find_element(By.XPATH,"//div[contains(@class, 'hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module')]/ul[contains(@class, 'footer__list')]").text



        EventName = list()
        EventDesc = list()
        EventDate = list()

        for i in range(len(RawEventName)):
            data = ItemLoader(item = GgventuresItem(), selector = i)
            data.add_value('university_name',university_name)
            data.add_value('university_contact_info',university_contact_info)
            data.add_value('logo',logo)
            # data['event_name']
            # data['event_date']
            # data['event_time']
            # data['event_link']
            # data['event_desc']
            # data['startups_name']
            # data['startups_link']
            # data['startups_contact_info']
            data.add_value('event_name', RawEventName[i].text)
            data.add_value('event_desc', RawEventDesc[i].text)
            data.add_value('event_date', RawEventDate[i].text.replace('\n',' '))
            yield data.load_item()

        self.driver.quit()
            # logger.info(f"Fetching Event Date: {RawEventDate[i].text.replace('\n',' ')}")


        # raw_page = Selector(text=response.page_source)
        # data = GgventuresItem()
        # data['event_name'] = response.xpath("//div[contains(@class, 'events__title')]")
        # logger.info(f"Fetching Event Name: {data['event_name']}")
