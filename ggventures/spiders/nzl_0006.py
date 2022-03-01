import scrapy


class Nzl0006Spider(scrapy.Spider):
    name = 'nzl_0006'
    allowed_domains = ['https://www.canterbury.ac.nz/business/']
    start_urls = ['http://https://www.canterbury.ac.nz/business//']

    def parse(self, response):
        pass
