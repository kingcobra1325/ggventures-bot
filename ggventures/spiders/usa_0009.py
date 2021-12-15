import scrapy


class Usa0009Spider(scrapy.Spider):
    name = 'usa-0009'
    allowed_domains = ['https://www.bu.edu/questrom/']
    start_urls = ['http://https://www.bu.edu/questrom//']

    def parse(self, response):
        pass
