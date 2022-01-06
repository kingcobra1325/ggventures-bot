import scrapy


class Usa0045Spider(scrapy.Spider):
    name = 'usa_0045'
    allowed_domains = ['https://www.marquette.edu/business/']
    start_urls = ['http://https://www.marquette.edu/business//']

    def parse(self, response):
        pass
