import scrapy


class Usa0078Spider(scrapy.Spider):
    name = 'usa_0078'
    allowed_domains = ['https://eller.arizona.edu/']
    start_urls = ['http://https://eller.arizona.edu//']

    def parse(self, response):
        pass
