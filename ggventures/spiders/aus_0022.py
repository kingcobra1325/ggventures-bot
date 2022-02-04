import scrapy


class Aus0022Spider(scrapy.Spider):
    name = 'aus_0022'
    allowed_domains = ['https://business.adelaide.edu.au/']
    start_urls = ['http://https://business.adelaide.edu.au//']

    def parse(self, response):
        pass
