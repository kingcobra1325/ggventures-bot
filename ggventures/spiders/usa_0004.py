import scrapy


class Usa0004Spider(scrapy.Spider):
    name = 'usa-0004'
    allowed_domains = ['https://www.babson.edu/']
    start_urls = ['http://https://www.babson.edu//']

    def parse(self, response):
        pass
