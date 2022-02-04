import scrapy


class Aus0021Spider(scrapy.Spider):
    name = 'aus_0021'
    allowed_domains = ['https://www.unisa.edu.au/business']
    start_urls = ['http://https://www.unisa.edu.au/business/']

    def parse(self, response):
        pass
