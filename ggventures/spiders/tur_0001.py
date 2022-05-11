import scrapy


class Tur0001Spider(scrapy.Spider):
    name = 'tur_0001'
    allowed_domains = ['http://fba.bilkent.edu.tr/']
    start_urls = ['http://http://fba.bilkent.edu.tr//']

    def parse(self, response):
        pass
