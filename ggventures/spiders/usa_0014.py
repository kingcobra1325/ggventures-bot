import scrapy


class Usa0014Spider(scrapy.Spider):
    name = 'usa_0014'
    allowed_domains = ['https://www.cmu.edu/tepper/']
    start_urls = ['http://https://www.cmu.edu/tepper//']

    def parse(self, response):
        pass
