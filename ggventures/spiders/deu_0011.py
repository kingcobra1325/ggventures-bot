import scrapy


class Deu0011Spider(scrapy.Spider):
    name = 'deu_0011'
    allowed_domains = ['https://www.gisma.com/']
    start_urls = ['http://https://www.gisma.com//']

    def parse(self, response):
        pass
