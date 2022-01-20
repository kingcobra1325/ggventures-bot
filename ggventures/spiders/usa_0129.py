import scrapy


class Usa0129Spider(scrapy.Spider):
    name = 'usa_0129'
    allowed_domains = ['https://www.wharton.upenn.edu/']
    start_urls = ['http://https://www.wharton.upenn.edu//']

    def parse(self, response):
        pass
