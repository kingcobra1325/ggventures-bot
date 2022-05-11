import scrapy


class Tur0003Spider(scrapy.Spider):
    name = 'tur_0003'
    allowed_domains = ['https://www.gsu.edu.tr/']
    start_urls = ['http://https://www.gsu.edu.tr//']

    def parse(self, response):
        pass
