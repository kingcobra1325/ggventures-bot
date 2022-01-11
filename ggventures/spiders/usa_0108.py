import scrapy


class Usa0108Spider(scrapy.Spider):
    name = 'usa_0108'
    allowed_domains = ['https://www.business.uconn.edu/']
    start_urls = ['http://https://www.business.uconn.edu//']

    def parse(self, response):
        pass
