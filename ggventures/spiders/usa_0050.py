import scrapy


class Usa0050Spider(scrapy.Spider):
    name = 'usa_0050'
    allowed_domains = ['https://management.njit.edu/']
    start_urls = ['http://https://management.njit.edu//']

    def parse(self, response):
        pass
