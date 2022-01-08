import scrapy


class Usa0079Spider(scrapy.Spider):
    name = 'usa_0079'
    allowed_domains = ['https://www.chicagobooth.edu/']
    start_urls = ['http://https://www.chicagobooth.edu//']

    def parse(self, response):
        pass
