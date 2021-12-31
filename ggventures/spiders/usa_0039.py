import scrapy


class Usa0039Spider(scrapy.Spider):
    name = 'usa_0039'
    allowed_domains = ['https://cba.k-state.edu/']
    start_urls = ['http://https://cba.k-state.edu//']

    def parse(self, response):
        pass
