import scrapy


class Usa0048Spider(scrapy.Spider):
    name = 'usa_0048'
    allowed_domains = ['https://mitsloan.mit.edu/']
    start_urls = ['http://https://mitsloan.mit.edu//']

    def parse(self, response):
        pass
