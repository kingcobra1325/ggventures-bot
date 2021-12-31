import scrapy


class Usa0040Spider(scrapy.Spider):
    name = 'usa_0040'
    allowed_domains = ['https://business.lehigh.edu/']
    start_urls = ['http://https://business.lehigh.edu//']

    def parse(self, response):
        pass
