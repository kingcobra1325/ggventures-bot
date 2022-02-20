import scrapy


class Aus0034Spider(scrapy.Spider):
    name = 'aus_0034'
    allowed_domains = ['https://www.uow.edu.au/business-law/']
    start_urls = ['http://https://www.uow.edu.au/business-law//']

    def parse(self, response):
        pass
