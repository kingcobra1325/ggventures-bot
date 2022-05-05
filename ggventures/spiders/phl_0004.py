import scrapy


class Phl0004Spider(scrapy.Spider):
    name = 'phl_0004'
    allowed_domains = ['https://www.usc.edu.ph/']
    start_urls = ['http://https://www.usc.edu.ph//']

    def parse(self, response):
        pass
