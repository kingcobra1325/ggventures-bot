import scrapy


class Nzl0008Spider(scrapy.Spider):
    name = 'nzl_0008'
    allowed_domains = ['https://www.wgtn.ac.nz/']
    start_urls = ['http://https://www.wgtn.ac.nz//']

    def parse(self, response):
        pass
