import scrapy


class Bra0004Spider(scrapy.Spider):
    name = 'bra_0004'
    allowed_domains = ['https://eaesp.fgv.br/en']
    start_urls = ['http://https://eaesp.fgv.br/en/']

    def parse(self, response):
        pass
