import scrapy


class Usa0013Spider(scrapy.Spider):
    name = 'usa_0013'
    allowed_domains = ['https://www.csulb.edu/']
    start_urls = ['http://https://www.csulb.edu//']

    def parse(self, response):
        pass
