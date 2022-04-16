import scrapy


class Mex0016Spider(scrapy.Spider):
    name = 'mex_0016'
    allowed_domains = ['https://www.udem.edu.mx/en/business/business']
    start_urls = ['http://https://www.udem.edu.mx/en/business/business/']

    def parse(self, response):
        pass
