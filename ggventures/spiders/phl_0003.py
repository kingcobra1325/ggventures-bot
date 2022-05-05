import scrapy


class Phl0003Spider(scrapy.Spider):
    name = 'phl_0003'
    allowed_domains = ['https://www.dlsu.edu.ph/colleges/soe/']
    start_urls = ['http://https://www.dlsu.edu.ph/colleges/soe//']

    def parse(self, response):
        pass
