import scrapy


class Usa0119Spider(scrapy.Spider):
    name = 'usa_0119'
    allowed_domains = ['https://www.rhsmith.umd.edu/']
    start_urls = ['http://https://www.rhsmith.umd.edu//']

    def parse(self, response):
        pass
