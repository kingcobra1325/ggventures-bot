import scrapy


class Usa0096Spider(scrapy.Spider):
    name = 'usa_0096'
    allowed_domains = ['https://freeman.tulane.edu/']
    start_urls = ['http://https://freeman.tulane.edu//']

    def parse(self, response):
        pass
