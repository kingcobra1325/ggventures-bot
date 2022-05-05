import scrapy


class Phl0001Spider(scrapy.Spider):
    name = 'phl_0001'
    allowed_domains = ['https://www.aim.edu/']
    start_urls = ['http://https://www.aim.edu//']

    def parse(self, response):
        pass
