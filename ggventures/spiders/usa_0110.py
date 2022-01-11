import scrapy


class Usa0110Spider(scrapy.Spider):
    name = 'usa_0110'
    allowed_domains = ['https://daniels.du.edu/']
    start_urls = ['http://https://daniels.du.edu//']

    def parse(self, response):
        pass
