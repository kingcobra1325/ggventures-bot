import scrapy


class Usa0003Spider(scrapy.Spider):
    name = 'usa-0003'
    allowed_domains = ['https://www.auburn.edu/']
    start_urls = ['http://https://www.auburn.edu//']

    def parse(self, response):
        pass
