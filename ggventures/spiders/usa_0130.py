import scrapy


class Usa0130Spider(scrapy.Spider):
    name = 'usa_0130'
    allowed_domains = ['https://business.pitt.edu/']
    start_urls = ['http://https://business.pitt.edu//']

    def parse(self, response):
        pass
