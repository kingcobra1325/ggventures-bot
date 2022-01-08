import scrapy


class Usa0089Spider(scrapy.Spider):
    name = 'usa_0089'
    allowed_domains = ['https://www.usd.edu/business']
    start_urls = ['http://https://www.usd.edu/business/']

    def parse(self, response):
        pass
