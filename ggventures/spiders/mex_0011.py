import scrapy


class Mex0011Spider(scrapy.Spider):
    name = 'mex_0011'
    allowed_domains = ['http://www.fca.uaslp.mx/']
    start_urls = ['http://http://www.fca.uaslp.mx//']

    def parse(self, response):
        pass
