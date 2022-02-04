import scrapy


class Aus0026Spider(scrapy.Spider):
    name = 'aus_0026'
    allowed_domains = ['https://business.uq.edu.au/']
    start_urls = ['http://https://business.uq.edu.au//']

    def parse(self, response):
        pass
