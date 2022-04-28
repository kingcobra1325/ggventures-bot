import scrapy


class Bra0007Spider(scrapy.Spider):
    name = 'bra_0007'
    allowed_domains = ['http://us.fia.com.br/']
    start_urls = ['http://http://us.fia.com.br//']

    def parse(self, response):
        pass
