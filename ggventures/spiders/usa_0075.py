import scrapy


class Usa0075Spider(scrapy.Spider):
    name = 'usa_0075'
    allowed_domains = ['https://business.gwu.edu/']
    start_urls = ['http://https://business.gwu.edu//']

    def parse(self, response):
        pass
