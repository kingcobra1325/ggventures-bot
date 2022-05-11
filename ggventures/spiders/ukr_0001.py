import scrapy


class Ukr0001Spider(scrapy.Spider):
    name = 'ukr_0001'
    allowed_domains = ['https://www.iiba.org/']
    start_urls = ['http://https://www.iiba.org//']

    def parse(self, response):
        pass
