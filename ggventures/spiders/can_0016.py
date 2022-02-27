import scrapy


class Can0016Spider(scrapy.Spider):
    name = 'can_0016'
    allowed_domains = ['https://www.sauder.ubc.ca/']
    start_urls = ['http://https://www.sauder.ubc.ca//']

    def parse(self, response):
        pass
