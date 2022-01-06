import scrapy


class Usa0060Spider(scrapy.Spider):
    name = 'usa_0060'
    allowed_domains = ['https://saunders.rit.edu/']
    start_urls = ['http://https://saunders.rit.edu//']

    def parse(self, response):
        pass
