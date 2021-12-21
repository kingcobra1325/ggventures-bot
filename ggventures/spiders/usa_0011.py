import scrapy


class Usa0011Spider(scrapy.Spider):
    name = 'usa_0011'
    allowed_domains = ['https://marriott.byu.edu/']
    start_urls = ['http://https://marriott.byu.edu//']

    def parse(self, response):
        pass
