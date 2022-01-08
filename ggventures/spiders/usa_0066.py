import scrapy


class Usa0066Spider(scrapy.Spider):
    name = 'usa_0066'
    allowed_domains = ['https://www.shu.edu/business/']
    start_urls = ['http://https://www.shu.edu/business//']

    def parse(self, response):
        pass
