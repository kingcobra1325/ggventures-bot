import scrapy


class Vnm0003Spider(scrapy.Spider):
    name = 'vnm_0003'
    allowed_domains = ['https://hsb.edu.vn/en/']
    start_urls = ['http://https://hsb.edu.vn/en//']

    def parse(self, response):
        pass
