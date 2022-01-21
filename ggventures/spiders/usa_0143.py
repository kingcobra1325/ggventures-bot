import scrapy


class Usa0143Spider(scrapy.Spider):
    name = 'usa_0143'
    allowed_domains = ['https://business.wisc.edu/']
    start_urls = ['http://https://business.wisc.edu//']

    def parse(self, response):
        pass
