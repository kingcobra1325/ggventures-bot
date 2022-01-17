import scrapy


class Usa0124Spider(scrapy.Spider):
    name = 'usa_0124'
    allowed_domains = ['https://business.missouri.edu/']
    start_urls = ['http://https://business.missouri.edu//']

    def parse(self, response):
        pass
