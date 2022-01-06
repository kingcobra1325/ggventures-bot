import scrapy


class Usa0046Spider(scrapy.Spider):
    name = 'usa_0046'
    allowed_domains = ['https://broad.msu.edu/']
    start_urls = ['http://https://broad.msu.edu//']

    def parse(self, response):
        pass
