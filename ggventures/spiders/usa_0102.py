import scrapy


class Usa0102Spider(scrapy.Spider):
    name = 'usa_0102'
    allowed_domains = ['https://haas.berkeley.edu/']
    start_urls = ['http://https://haas.berkeley.edu//']

    def parse(self, response):
        pass
