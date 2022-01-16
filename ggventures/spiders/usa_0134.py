import scrapy


class Usa0134Spider(scrapy.Spider):
    name = 'usa_0134'
    allowed_domains = ['https://www.usfca.edu/management']
    start_urls = ['http://https://www.usfca.edu/management/']

    def parse(self, response):
        pass
