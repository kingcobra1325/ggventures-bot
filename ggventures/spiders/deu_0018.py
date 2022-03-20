import scrapy


class Deu0018Spider(scrapy.Spider):
    name = 'deu_0018'
    allowed_domains = ['https://www.wi.tum.de/']
    start_urls = ['http://https://www.wi.tum.de//']

    def parse(self, response):
        pass
