import scrapy


class Usa0132Spider(scrapy.Spider):
    name = 'usa_0132'
    allowed_domains = ['http://simon.rochester.edu/']
    start_urls = ['http://http://simon.rochester.edu//']

    def parse(self, response):
        pass
