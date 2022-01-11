import scrapy


class Usa0120Spider(scrapy.Spider):
    name = 'usa_0120'
    allowed_domains = ['https://www.isenberg.umass.edu/']
    start_urls = ['http://https://www.isenberg.umass.edu//']

    def parse(self, response):
        pass
