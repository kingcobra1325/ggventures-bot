import scrapy


class Usa0092Spider(scrapy.Spider):
    name = 'usa_0092'
    allowed_domains = ['https://jindal.utdallas.edu/']
    start_urls = ['http://https://jindal.utdallas.edu//']

    def parse(self, response):
        pass
