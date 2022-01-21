import scrapy


class Usa0148Spider(scrapy.Spider):
    name = 'usa_0148'
    allowed_domains = ['https://business.wfu.edu/']
    start_urls = ['http://https://business.wfu.edu//']

    def parse(self, response):
        pass
