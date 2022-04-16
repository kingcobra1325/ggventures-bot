import scrapy


class Mex0009Spider(scrapy.Spider):
    name = 'mex_0009'
    allowed_domains = ['https://www.anahuac.mx/']
    start_urls = ['http://https://www.anahuac.mx//']

    def parse(self, response):
        pass
