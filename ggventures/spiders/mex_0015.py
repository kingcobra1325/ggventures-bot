import scrapy


class Mex0015Spider(scrapy.Spider):
    name = 'mex_0015'
    allowed_domains = ['https://www.udlap.mx/']
    start_urls = ['http://https://www.udlap.mx//']

    def parse(self, response):
        pass
