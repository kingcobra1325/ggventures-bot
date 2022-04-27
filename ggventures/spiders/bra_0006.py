import scrapy


class Bra0006Spider(scrapy.Spider):
    name = 'bra_0006'
    allowed_domains = ['https://www.fea.usp.br/']
    start_urls = ['http://https://www.fea.usp.br//']

    def parse(self, response):
        pass
