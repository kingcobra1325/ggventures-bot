import scrapy


class Usa0133Spider(scrapy.Spider):
    name = 'usa_0133'
    allowed_domains = ['https://www.sandiego.edu/business/']
    start_urls = ['http://https://www.sandiego.edu/business//']

    def parse(self, response):
        pass
