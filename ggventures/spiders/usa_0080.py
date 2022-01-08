import scrapy


class Usa0080Spider(scrapy.Spider):
    name = 'usa_0080'
    allowed_domains = ['https://tippie.uiowa.edu/']
    start_urls = ['http://https://tippie.uiowa.edu//']

    def parse(self, response):
        pass
