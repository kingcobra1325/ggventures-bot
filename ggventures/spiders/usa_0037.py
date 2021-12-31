import scrapy


class Usa0037Spider(scrapy.Spider):
    name = 'usa_0037'
    allowed_domains = ['https://kelley.iu.edu/']
    start_urls = ['http://https://kelley.iu.edu//']

    def parse(self, response):
        pass
