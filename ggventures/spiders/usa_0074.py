import scrapy


class Usa0074Spider(scrapy.Spider):
    name = 'usa_0074'
    allowed_domains = ['https://www.tamu.edu/']
    start_urls = ['http://https://www.tamu.edu//']

    def parse(self, response):
        pass
