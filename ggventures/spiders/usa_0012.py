import scrapy, time
# from scrapy import Selector

from bot_email import missing_info_email, error_email

from binaries import Load_Driver, logger, WebScroller

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0012Spider(scrapy.Spider):
    name = 'usa_0012'
    start_urls = ['https://www.csuchico.edu/cob/events/index.shtml']

    def parse(self, response):
        pass
