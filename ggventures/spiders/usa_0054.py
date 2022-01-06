import scrapy


class Usa0054Spider(scrapy.Spider):
    name = 'usa_0054'
    allowed_domains = ['https://business.okstate.edu/']
    start_urls = ['http://https://business.okstate.edu//']

    def parse(self, response):
        pass
