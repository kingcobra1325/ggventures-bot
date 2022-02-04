import scrapy


class Aus0012Spider(scrapy.Spider):
    name = 'aus_0012'
    allowed_domains = ['https://mbs.edu/']
    start_urls = ['http://https://mbs.edu//']

    def parse(self, response):
        pass
