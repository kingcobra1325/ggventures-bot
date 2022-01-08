import scrapy


class Usa0077Spider(scrapy.Spider):
    name = 'usa_0077'
    allowed_domains = ['https://www.smeal.psu.edu/']
    start_urls = ['http://https://www.smeal.psu.edu//']

    def parse(self, response):
        pass
