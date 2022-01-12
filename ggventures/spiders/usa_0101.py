import scrapy


class Usa0101Spider(scrapy.Spider):
    name = 'usa_0101'
    allowed_domains = ['https://ualr.edu/business/']
    start_urls = ['http://https://ualr.edu/business//']

    def parse(self, response):
        pass
