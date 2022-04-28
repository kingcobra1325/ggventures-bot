import scrapy


class Bra0008Spider(scrapy.Spider):
    name = 'bra_0008'
    allowed_domains = ['https://www.fdc.org.br/']
    start_urls = ['http://https://www.fdc.org.br//']

    def parse(self, response):
        pass
