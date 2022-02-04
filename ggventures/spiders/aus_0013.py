import scrapy


class Aus0013Spider(scrapy.Spider):
    name = 'aus_0013'
    allowed_domains = ['https://www.monash.edu/business']
    start_urls = ['http://https://www.monash.edu/business/']

    def parse(self, response):
        pass
