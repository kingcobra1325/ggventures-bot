import scrapy


class Bra0014Spider(scrapy.Spider):
    name = 'bra_0014'
    allowed_domains = ['http://www.sociaisaplicadas.ufpr.br/portal/administracao/']
    start_urls = ['http://http://www.sociaisaplicadas.ufpr.br/portal/administracao//']

    def parse(self, response):
        pass
