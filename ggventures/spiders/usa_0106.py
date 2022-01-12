import scrapy


class Usa0106Spider(scrapy.Spider):
    name = 'usa_0106'
    allowed_domains = ['https://business.ucr.edu/graduate']
    start_urls = ['http://https://business.ucr.edu/graduate/']

    def parse(self, response):
        pass
