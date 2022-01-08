import scrapy


class Usa0073Spider(scrapy.Spider):
    name = 'usa_0073'
    allowed_domains = ['https://www.fox.temple.edu/']
    start_urls = ['http://https://www.fox.temple.edu//']

    def parse(self, response):
        pass
