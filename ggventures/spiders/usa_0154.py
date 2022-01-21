import scrapy


class Usa0154Spider(scrapy.Spider):
    name = 'usa_0154'
    allowed_domains = ['https://som.yale.edu/']
    start_urls = ['http://https://som.yale.edu//']

    def parse(self, response):
        pass
