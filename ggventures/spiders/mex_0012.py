import scrapy


class Mex0012Spider(scrapy.Spider):
    name = 'mex_0012'
    allowed_domains = ['https://www.uam.mx/lang/eng/index.html']
    start_urls = ['http://https://www.uam.mx/lang/eng/index.html/']

    def parse(self, response):
        pass
