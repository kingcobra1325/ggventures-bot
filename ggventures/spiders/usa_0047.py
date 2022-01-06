import scrapy


class Usa0047Spider(scrapy.Spider):
    name = 'usa_0047'
    allowed_domains = ['https://www.business.msstate.edu/']
    start_urls = ['http://https://www.business.msstate.edu//']

    def parse(self, response):
        pass
