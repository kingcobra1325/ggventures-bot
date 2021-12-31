import scrapy


class Usa0034Spider(scrapy.Spider):
    name = 'usa_0034'
    allowed_domains = ['https://www.hbs.edu/']
    start_urls = ['http://https://www.hbs.edu//']

    def parse(self, response):
        pass
