import scrapy


class Usa0118Spider(scrapy.Spider):
    name = 'usa_0118'
    allowed_domains = ['https://umaine.edu/business/']
    start_urls = ['http://https://umaine.edu/business//']

    def parse(self, response):
        pass
