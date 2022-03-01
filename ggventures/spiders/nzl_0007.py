import scrapy


class Nzl0007Spider(scrapy.Spider):
    name = 'nzl_0007'
    allowed_domains = ['https://www.otago.ac.nz/business/']
    start_urls = ['http://https://www.otago.ac.nz/business//']

    def parse(self, response):
        pass
