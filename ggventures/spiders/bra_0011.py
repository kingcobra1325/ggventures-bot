import scrapy


class Bra0011Spider(scrapy.Spider):
    name = 'bra_0011'
    allowed_domains = ['https://iag.puc-rio.br/en/home_en/']
    start_urls = ['http://https://iag.puc-rio.br/en/home_en//']

    def parse(self, response):
        pass
