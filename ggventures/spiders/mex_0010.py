import scrapy


class Mex0010Spider(scrapy.Spider):
    name = 'mex_0010'
    allowed_domains = ['http://facpya.uanl.mx/']
    start_urls = ['http://http://facpya.uanl.mx//']

    def parse(self, response):
        pass
