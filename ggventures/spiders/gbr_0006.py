import scrapy


class Gbr0006Spider(scrapy.Spider):
    name = 'gbr_0006'
    allowed_domains = ['https://www.cardiff.ac.uk/business-school']
    start_urls = ['http://https://www.cardiff.ac.uk/business-school/']

    def parse(self, response):
        pass
