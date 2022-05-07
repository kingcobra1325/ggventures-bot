import scrapy


class Che0004Spider(scrapy.Spider):
    name = 'che_0004'
    allowed_domains = ['https://www.imd.org/']
    start_urls = ['http://https://www.imd.org//']

    def parse(self, response):
        pass
