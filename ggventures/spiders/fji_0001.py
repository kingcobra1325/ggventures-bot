import scrapy


class Fji0001Spider(scrapy.Spider):
    name = 'fji_0001'
    allowed_domains = ['http://www.fbe.usp.ac.fj/']
    start_urls = ['http://http://www.fbe.usp.ac.fj//']

    def parse(self, response):
        pass
