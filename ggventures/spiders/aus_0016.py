import scrapy


class Aus0016Spider(scrapy.Spider):
    name = 'aus_0016'
    allowed_domains = ['https://www.rmit.edu.au/about/schools-colleges/management']
    start_urls = ['http://https://www.rmit.edu.au/about/schools-colleges/management/']

    def parse(self, response):
        pass
