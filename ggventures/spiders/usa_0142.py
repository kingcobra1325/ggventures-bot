import scrapy


class Usa0142Spider(scrapy.Spider):
    name = 'usa_0142'
    allowed_domains = ['https://foster.uw.edu/']
    start_urls = ['http://https://foster.uw.edu//']

    def parse(self, response):
        pass
