import scrapy


class Usa0103Spider(scrapy.Spider):
    name = 'usa_0103'
    allowed_domains = ['https://gsm.ucdavis.edu/']
    start_urls = ['http://https://gsm.ucdavis.edu//']

    def parse(self, response):
        pass
