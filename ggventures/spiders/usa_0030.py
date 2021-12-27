import scrapy


class Usa0030Spider(scrapy.Spider):
    name = 'usa_0030'
    allowed_domains = ['https://business.gmu.edu/']
    start_urls = ['http://https://business.gmu.edu//']

    def parse(self, response):
        pass
