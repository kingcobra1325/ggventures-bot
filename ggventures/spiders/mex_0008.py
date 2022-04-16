import scrapy


class Mex0008Spider(scrapy.Spider):
    name = 'mex_0008'
    allowed_domains = ['https://www.anahuac.mx/']
    start_urls = ['http://https://www.anahuac.mx//']

    def parse(self, response):
        pass
