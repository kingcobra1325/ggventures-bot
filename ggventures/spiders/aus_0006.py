import scrapy


class Aus0006Spider(scrapy.Spider):
    name = 'aus_0006'
    allowed_domains = ['https://about.curtin.edu.au/learning-teaching/business-and-law/']
    start_urls = ['http://https://about.curtin.edu.au/learning-teaching/business-and-law//']

    def parse(self, response):
        pass
