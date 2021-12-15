import scrapy


class Usa0007Spider(scrapy.Spider):
    name = 'usa-0007'
    allowed_domains = ['https://www.bentley.edu/']
    start_urls = ['http://https://www.bentley.edu//']

    def parse(self, response):
        pass
