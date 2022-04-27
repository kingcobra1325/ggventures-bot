import scrapy


class Bra0009Spider(scrapy.Spider):
    name = 'bra_0009'
    allowed_domains = ['https://www.ibmec.br/sp']
    start_urls = ['http://https://www.ibmec.br/sp/']

    def parse(self, response):
        pass
