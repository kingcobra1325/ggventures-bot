import scrapy


class Deu0016Spider(scrapy.Spider):
    name = 'deu_0016'
    allowed_domains = ['https://www.rwth-aachen.de/']
    start_urls = ['http://https://www.rwth-aachen.de//']

    def parse(self, response):
        pass
