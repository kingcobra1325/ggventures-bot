import scrapy


class Usa0099Spider(scrapy.Spider):
    name = 'usa_0099'
    allowed_domains = ['https://business.uaa.alaska.edu/']
    start_urls = ['http://https://business.uaa.alaska.edu//']

    def parse(self, response):
        pass
