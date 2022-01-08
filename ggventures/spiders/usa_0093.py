import scrapy


class Usa0093Spider(scrapy.Spider):
    name = 'usa_0093'
    allowed_domains = ['https://business.utsa.edu/']
    start_urls = ['http://https://business.utsa.edu//']

    def parse(self, response):
        pass
