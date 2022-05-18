import scrapy


class Vnm0002Spider(scrapy.Spider):
    name = 'vnm_0002'
    allowed_domains = ['https://ueh.edu.vn/en/']
    start_urls = ['http://https://ueh.edu.vn/en//']

    def parse(self, response):
        pass
