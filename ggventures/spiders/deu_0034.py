import scrapy


class Deu0034Spider(scrapy.Spider):
    name = 'deu_0034'
    allowed_domains = ['https://wiso.uni-koeln.de/en/']
    start_urls = ['http://https://wiso.uni-koeln.de/en//']

    def parse(self, response):
        pass
