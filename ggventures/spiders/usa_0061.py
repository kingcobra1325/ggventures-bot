import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email, unique_event

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Usa0061Spider(scrapy.Spider):
    name = 'usa_0061'
    allowed_domains = ['https://www.business.rutgers.edu/']
    start_urls = ['http://https://www.business.rutgers.edu//']

    def parse(self, response):
        pass
