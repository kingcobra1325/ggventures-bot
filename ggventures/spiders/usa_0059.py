import scrapy


class Usa0059Spider(scrapy.Spider):
    name = 'usa_0059'
    allowed_domains = ['https://business.rice.edu/']
    start_urls = ['http://https://business.rice.edu//']

    def parse(self, response):
        pass
