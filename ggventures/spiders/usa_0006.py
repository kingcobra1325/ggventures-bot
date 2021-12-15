import scrapy


class Usa0006Spider(scrapy.Spider):
    name = 'usa-0006'
    allowed_domains = ['https://www.baylor.edu/business/']
    start_urls = ['http://https://www.baylor.edu/business//']

    def parse(self, response):
        pass
