import scrapy


class Usa0068Spider(scrapy.Spider):
    name = 'usa_0068'
    allowed_domains = ['https://siu.edu/']
    start_urls = ['http://https://siu.edu//']

    def parse(self, response):
        pass
