import scrapy


class Tur0006Spider(scrapy.Spider):
    name = 'tur_0006'
    allowed_domains = ['https://gsb.ku.edu.tr/']
    start_urls = ['http://https://gsb.ku.edu.tr//']

    def parse(self, response):
        pass
