import scrapy


class Usa0002Spider(scrapy.Spider):
    name = 'usa-0002'
    allowed_domains = ['https://wpcarey.asu.edu/']
    start_urls = ['http://https://wpcarey.asu.edu//']

    def parse(self, response):
        pass
