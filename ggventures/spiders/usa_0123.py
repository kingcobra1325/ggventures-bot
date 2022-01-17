import scrapy


class Usa0123Spider(scrapy.Spider):
    name = 'usa_0123'
    allowed_domains = ['https://business.olemiss.edu/']
    start_urls = ['http://https://business.olemiss.edu//']

    def parse(self, response):
        pass
