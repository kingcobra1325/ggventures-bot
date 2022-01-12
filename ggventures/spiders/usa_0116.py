import scrapy


class Usa0116Spider(scrapy.Spider):
    name = 'usa_0116'
    allowed_domains = ['https://gatton.uky.edu/']
    start_urls = ['http://https://gatton.uky.edu//']

    def parse(self, response):
        pass
