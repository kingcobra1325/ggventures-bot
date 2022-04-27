import scrapy


class Bra0016Spider(scrapy.Spider):
    name = 'bra_0016'
    allowed_domains = ['http://www.ufrgs.br/ufrgs/inicial']
    start_urls = ['http://http://www.ufrgs.br/ufrgs/inicial/']

    def parse(self, response):
        pass
