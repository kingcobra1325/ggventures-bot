import scrapy


class Usa0139Spider(scrapy.Spider):
    name = 'usa_0139'
    allowed_domains = ['https://eccles.utah.edu/']
    start_urls = ['http://https://eccles.utah.edu//']

    def parse(self, response):
        pass
