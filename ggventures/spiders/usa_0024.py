import scrapy


class Usa0024Spider(scrapy.Spider):
    name = 'usa_0024'
    allowed_domains = ['https://www.lebow.drexel.edu/']
    start_urls = ['http://https://www.lebow.drexel.edu//']

    def parse(self, response):
        pass
