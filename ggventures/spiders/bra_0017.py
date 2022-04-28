import scrapy


class Bra0017Spider(scrapy.Spider):
    name = 'bra_0017'
    allowed_domains = ['https://www.mackenzie.br/universidade/unidades-academicas/ccsa']
    start_urls = ['http://https://www.mackenzie.br/universidade/unidades-academicas/ccsa/']

    def parse(self, response):
        pass
