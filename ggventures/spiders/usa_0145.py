import scrapy


class Usa0145Spider(scrapy.Spider):
    name = 'usa_0145'
    allowed_domains = ['https://business.vanderbilt.edu/']
    start_urls = ['http://https://business.vanderbilt.edu//']

    def parse(self, response):
        pass
