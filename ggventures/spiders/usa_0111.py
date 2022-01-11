import scrapy


class Usa0111Spider(scrapy.Spider):
    name = 'usa_0111'
    allowed_domains = ['https://warrington.ufl.edu/']
    start_urls = ['http://https://warrington.ufl.edu//']

    def parse(self, response):
        pass
