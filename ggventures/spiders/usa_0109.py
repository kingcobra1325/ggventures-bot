import scrapy


class Usa0109Spider(scrapy.Spider):
    name = 'usa_0109'
    allowed_domains = ['https://lerner.udel.edu/']
    start_urls = ['http://https://lerner.udel.edu//']

    def parse(self, response):
        pass
