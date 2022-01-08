import scrapy


class Usa0098Spider(scrapy.Spider):
    name = 'usa_0098'
    allowed_domains = ['https://www.uab.edu/business/home/']
    start_urls = ['http://https://www.uab.edu/business/home//']

    def parse(self, response):
        pass
