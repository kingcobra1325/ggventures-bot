import scrapy


class Bra0005Spider(scrapy.Spider):
    name = 'bra_0005'
    allowed_domains = ['https://ebape.fgv.br/en']
    start_urls = ['http://https://ebape.fgv.br/en/']

    def parse(self, response):
        pass
