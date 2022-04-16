import scrapy


class Mex0006Spider(scrapy.Spider):
    name = 'mex_0006'
    allowed_domains = ['https://tec.mx/en/san-luis-potosi-campus']
    start_urls = ['http://https://tec.mx/en/san-luis-potosi-campus/']

    def parse(self, response):
        pass
