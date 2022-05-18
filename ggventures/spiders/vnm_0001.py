import scrapy


class Vnm0001Spider(scrapy.Spider):
    name = 'vnm_0001'
    allowed_domains = ['https://www.cfvg.org/']
    start_urls = ['http://https://www.cfvg.org//']

    def parse(self, response):
        pass
