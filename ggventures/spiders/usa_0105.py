import scrapy


class Usa0105Spider(scrapy.Spider):
    name = 'usa_0105'
    allowed_domains = ['https://www.anderson.ucla.edu/']
    start_urls = ['http://https://www.anderson.ucla.edu//']

    def parse(self, response):
        pass
