import scrapy


class Usa0043Spider(scrapy.Spider):
    name = 'usa_0043'
    allowed_domains = ['https://www.lmu.edu/']
    start_urls = ['http://https://www.lmu.edu//']

    def parse(self, response):
        pass
