import scrapy


class Usa0083Spider(scrapy.Spider):
    name = 'usa_0083'
    allowed_domains = ['https://www.business.umt.edu/']
    start_urls = ['http://https://www.business.umt.edu//']

    def parse(self, response):
        pass
