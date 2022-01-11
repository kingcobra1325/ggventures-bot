import scrapy


class Usa0104Spider(scrapy.Spider):
    name = 'usa_0104'
    allowed_domains = ['https://merage.uci.edu/']
    start_urls = ['http://https://merage.uci.edu//']

    def parse(self, response):
        pass
