import scrapy


class Mex0005Spider(scrapy.Spider):
    name = 'mex_0005'
    allowed_domains = ['https://tec.mx/en/queretaro-campus']
    start_urls = ['http://https://tec.mx/en/queretaro-campus/']

    def parse(self, response):
        pass
