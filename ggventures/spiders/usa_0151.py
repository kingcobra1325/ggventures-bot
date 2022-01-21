import scrapy


class Usa0151Spider(scrapy.Spider):
    name = 'usa_0151'
    allowed_domains = ['https://business.wvu.edu/']
    start_urls = ['http://https://business.wvu.edu//']

    def parse(self, response):
        pass
