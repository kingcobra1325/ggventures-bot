import scrapy


class Aus0010Spider(scrapy.Spider):
    name = 'aus_0010'
    allowed_domains = ['https://www.latrobe.edu.au/business']
    start_urls = ['http://https://www.latrobe.edu.au/business/']

    def parse(self, response):
        pass
