import scrapy


class Usa0065Spider(scrapy.Spider):
    name = 'usa_0065'
    allowed_domains = ['https://www.scu.edu/business/']
    start_urls = ['http://https://www.scu.edu/business//']

    def parse(self, response):
        pass
