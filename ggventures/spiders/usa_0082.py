import scrapy


class Usa0082Spider(scrapy.Spider):
    name = 'usa_0082'
    allowed_domains = ['https://michiganross.umich.edu/']
    start_urls = ['http://https://michiganross.umich.edu//']

    def parse(self, response):
        pass
