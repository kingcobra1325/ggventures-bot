import scrapy


class Usa0026Spider(scrapy.Spider):
    name = 'usa_0026'
    allowed_domains = ['https://goizueta.emory.edu/']
    start_urls = ['http://https://goizueta.emory.edu//']

    def parse(self, response):
        pass
