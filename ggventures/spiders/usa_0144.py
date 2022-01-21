import scrapy


class Usa0144Spider(scrapy.Spider):
    name = 'usa_0144'
    allowed_domains = ['http://www.uwyo.edu/business/']
    start_urls = ['http://http://www.uwyo.edu/business//']

    def parse(self, response):
        pass
