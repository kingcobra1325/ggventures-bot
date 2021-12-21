import scrapy


class Usa0017Spider(scrapy.Spider):
    name = 'usa_0017'
    allowed_domains = ['https://www.clemson.edu/business/index.html']
    start_urls = ['http://https://www.clemson.edu/business/index.html/']

    def parse(self, response):
        pass
