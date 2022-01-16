import scrapy


class Usa0128Spider(scrapy.Spider):
    name = 'usa_0128'
    allowed_domains = ['https://business.uoregon.edu/']
    start_urls = ['http://https://business.uoregon.edu//']

    def parse(self, response):
        pass
