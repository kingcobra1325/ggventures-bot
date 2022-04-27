import scrapy


class Bra0015Spider(scrapy.Spider):
    name = 'bra_0015'
    allowed_domains = ['https://ea.ufba.br/en/']
    start_urls = ['http://https://ea.ufba.br/en//']

    def parse(self, response):
        pass
