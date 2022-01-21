import scrapy


class Usa0149Spider(scrapy.Spider):
    name = 'usa_0149'
    allowed_domains = ['https://business.wsu.edu/']
    start_urls = ['http://https://business.wsu.edu//']

    def parse(self, response):
        pass
