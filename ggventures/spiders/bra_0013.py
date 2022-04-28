import scrapy


class Bra0013Spider(scrapy.Spider):
    name = 'bra_0013'
    allowed_domains = ['https://www.ufpe.br/dca']
    start_urls = ['http://https://www.ufpe.br/dca/']

    def parse(self, response):
        pass
