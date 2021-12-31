import scrapy


class Usa0035Spider(scrapy.Spider):
    name = 'usa_0035'
    allowed_domains = ['https://www.hofstra.edu/business']
    start_urls = ['http://https://www.hofstra.edu/business/']

    def parse(self, response):
        pass
