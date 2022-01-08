import scrapy


class Usa0072Spider(scrapy.Spider):
    name = 'usa_0072'
    allowed_domains = ['https://whitman.syr.edu/']
    start_urls = ['http://https://whitman.syr.edu//']

    def parse(self, response):
        pass
