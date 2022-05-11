import scrapy


class Tur0004Spider(scrapy.Spider):
    name = 'tur_0004'
    allowed_domains = ['https://www.gau.edu.tr/en/']
    start_urls = ['http://https://www.gau.edu.tr/en//']

    def parse(self, response):
        pass
