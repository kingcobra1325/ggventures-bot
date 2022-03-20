import scrapy


class Deu0012Spider(scrapy.Spider):
    name = 'deu_0012'
    allowed_domains = ['https://www.hhl.de/']
    start_urls = ['http://https://www.hhl.de//']

    def parse(self, response):
        pass
