import scrapy


class Usa0088Spider(scrapy.Spider):
    name = 'usa_0088'
    allowed_domains = ['https://web.uri.edu/business/']
    start_urls = ['http://https://web.uri.edu/business//']

    def parse(self, response):
        pass
