import scrapy


class Usa0033Spider(scrapy.Spider):
    name = 'usa_0033'
    allowed_domains = ['https://robinson.gsu.edu/']
    start_urls = ['http://https://robinson.gsu.edu//']

    def parse(self, response):
        pass
