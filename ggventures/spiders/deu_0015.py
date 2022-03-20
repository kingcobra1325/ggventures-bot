import scrapy


class Deu0015Spider(scrapy.Spider):
    name = 'deu_0015'
    allowed_domains = ['https://www.en.som.lmu.de/']
    start_urls = ['http://https://www.en.som.lmu.de//']

    def parse(self, response):
        pass
