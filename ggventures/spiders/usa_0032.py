import scrapy


class Usa0032Spider(scrapy.Spider):
    name = 'usa_0032'
    allowed_domains = ['https://www.scheller.gatech.edu/index.html']
    start_urls = ['http://https://www.scheller.gatech.edu/index.html/']

    def parse(self, response):
        pass
