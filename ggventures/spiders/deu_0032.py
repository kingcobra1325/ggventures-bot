import scrapy


class Deu0032Spider(scrapy.Spider):
    name = 'deu_0032'
    allowed_domains = ['https://uni-tuebingen.de/']
    start_urls = ['http://https://uni-tuebingen.de//']

    def parse(self, response):
        pass
