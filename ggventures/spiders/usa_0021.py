import scrapy


class Usa0021Spider(scrapy.Spider):
    name = 'usa_0021'
    allowed_domains = ['https://www.creighton.edu/business']
    start_urls = ['http://https://www.creighton.edu/business/']

    def parse(self, response):
        pass
