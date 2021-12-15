import scrapy

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Usa0003Spider(scrapy.Spider):
    name = 'usa-0003'
    allowed_domains = ['https://calendar.auburn.edu/']
    start_urls = ['http://https://www.auburn.edu//']

    def parse(self, response):
        pass
