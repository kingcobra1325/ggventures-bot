import scrapy


class Usa0057Spider(scrapy.Spider):
    name = 'usa_0057'
    allowed_domains = ['https://krannert.purdue.edu/']
    start_urls = ['http://https://krannert.purdue.edu//']

    def parse(self, response):
        pass
