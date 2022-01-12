import scrapy


class Usa0114Spider(scrapy.Spider):
    name = 'usa_0114'
    allowed_domains = ['https://www.uidaho.edu/cbe']
    start_urls = ['http://https://www.uidaho.edu/cbe/']

    def parse(self, response):
        pass
