import scrapy


class Usa0147Spider(scrapy.Spider):
    name = 'usa_0147'
    allowed_domains = ['https://pamplin.vt.edu/']
    start_urls = ['http://https://pamplin.vt.edu//']

    def parse(self, response):
        pass
