import scrapy


class Usa0055Spider(scrapy.Spider):
    name = 'usa_0055'
    allowed_domains = ['https://lubin.pace.edu/']
    start_urls = ['http://https://lubin.pace.edu//']

    def parse(self, response):
        pass
