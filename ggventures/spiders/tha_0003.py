import scrapy


class Tha0003Spider(scrapy.Spider):
    name = 'tha_0003'
    allowed_domains = ['https://www.sasin.edu/']
    start_urls = ['http://https://www.sasin.edu//']

    def parse(self, response):
        pass
