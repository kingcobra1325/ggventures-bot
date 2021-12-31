import scrapy


class Usa0036Spider(scrapy.Spider):
    name = 'usa_0036'
    allowed_domains = ['https://business.howard.edu/']
    start_urls = ['http://https://business.howard.edu//']

    def parse(self, response):
        pass
