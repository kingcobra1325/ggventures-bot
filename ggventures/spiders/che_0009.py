import scrapy


class Che0009Spider(scrapy.Spider):
    name = 'che_0009'
    allowed_domains = ['https://www.unige.ch/']
    start_urls = ['http://https://www.unige.ch//']

    def parse(self, response):
        pass
