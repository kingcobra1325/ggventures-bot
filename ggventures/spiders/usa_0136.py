import scrapy


class Usa0136Spider(scrapy.Spider):
    name = 'usa_0136'
    allowed_domains = ['https://www.marshall.usc.edu/']
    start_urls = ['http://https://www.marshall.usc.edu//']

    def parse(self, response):
        pass
