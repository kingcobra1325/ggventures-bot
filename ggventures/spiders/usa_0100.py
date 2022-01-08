import scrapy


class Usa0100Spider(scrapy.Spider):
    name = 'usa_0100'
    allowed_domains = ['https://www.uaf.edu/cbsm/']
    start_urls = ['http://https://www.uaf.edu/cbsm//']

    def parse(self, response):
        pass
