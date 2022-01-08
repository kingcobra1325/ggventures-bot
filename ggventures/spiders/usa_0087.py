import scrapy


class Usa0087Spider(scrapy.Spider):
    name = 'usa_0087'
    allowed_domains = ['https://business.und.edu/']
    start_urls = ['http://https://business.und.edu//']

    def parse(self, response):
        pass
