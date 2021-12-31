import scrapy


class Usa0031Spider(scrapy.Spider):
    name = 'usa_0031'
    allowed_domains = ['https://msb.georgetown.edu/']
    start_urls = ['http://https://msb.georgetown.edu//']

    def parse(self, response):
        pass
