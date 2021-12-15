import scrapy


class Usa0001Spider(scrapy.Spider):
    name = 'usa-0001'
    allowed_domains = ['https://kogod.american.edu/']
    start_urls = ['http://https://kogod.american.edu//']

    def parse(self, response):
        pass
