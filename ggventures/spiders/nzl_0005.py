import scrapy


class Nzl0005Spider(scrapy.Spider):
    name = 'nzl_0005'
    allowed_domains = ['https://www.management.ac.nz/']
    start_urls = ['http://https://www.management.ac.nz//']

    def parse(self, response):
        pass
