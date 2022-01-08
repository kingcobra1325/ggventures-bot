import scrapy


class Usa0097Spider(scrapy.Spider):
    name = 'usa_0097'
    allowed_domains = ['https://management.buffalo.edu/']
    start_urls = ['http://https://management.buffalo.edu//']

    def parse(self, response):
        pass
