import scrapy


class Usa0127Spider(scrapy.Spider):
    name = 'usa_0127'
    allowed_domains = ['https://mendoza.nd.edu/']
    start_urls = ['http://https://mendoza.nd.edu//']

    def parse(self, response):
        pass
