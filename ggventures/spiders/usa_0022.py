import scrapy


class Usa0022Spider(scrapy.Spider):
    name = 'usa_0022'
    allowed_domains = ['https://www.tuck.dartmouth.edu/']
    start_urls = ['http://https://www.tuck.dartmouth.edu//']

    def parse(self, response):
        pass
