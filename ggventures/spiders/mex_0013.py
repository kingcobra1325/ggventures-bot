import scrapy


class Mex0013Spider(scrapy.Spider):
    name = 'mex_0013'
    allowed_domains = ['http://www.cucea.udg.mx/']
    start_urls = ['http://http://www.cucea.udg.mx//']

    def parse(self, response):
        pass
