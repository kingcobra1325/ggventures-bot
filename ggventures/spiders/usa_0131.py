import scrapy


class Usa0131Spider(scrapy.Spider):
    name = 'usa_0131'
    allowed_domains = ['https://robins.richmond.edu/']
    start_urls = ['http://https://robins.richmond.edu//']

    def parse(self, response):
        pass
