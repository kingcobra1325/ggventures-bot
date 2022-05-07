import scrapy


class Che0003Spider(scrapy.Spider):
    name = 'che_0003'
    allowed_domains = ['https://www.iimt.ch/']
    start_urls = ['http://https://www.iimt.ch//']

    def parse(self, response):
        pass
