import scrapy


class Mex0017Spider(scrapy.Spider):
    name = 'mex_0017'
    allowed_domains = ['https://www.fca.unam.mx/']
    start_urls = ['http://https://www.fca.unam.mx//']

    def parse(self, response):
        pass
