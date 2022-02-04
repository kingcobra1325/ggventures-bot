import scrapy


class Aus0020Spider(scrapy.Spider):
    name = 'aus_0020'
    allowed_domains = ['https://fbe.unimelb.edu.au/']
    start_urls = ['http://https://fbe.unimelb.edu.au//']

    def parse(self, response):
        pass
