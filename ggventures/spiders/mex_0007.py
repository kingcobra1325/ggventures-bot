import scrapy


class Mex0007Spider(scrapy.Spider):
    name = 'mex_0007'
    allowed_domains = ['https://tec.mx/en/toluca-campus']
    start_urls = ['http://https://tec.mx/en/toluca-campus/']

    def parse(self, response):
        pass
