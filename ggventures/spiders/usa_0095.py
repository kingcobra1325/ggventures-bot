import scrapy


class Usa0095Spider(scrapy.Spider):
    name = 'usa_0095'
    allowed_domains = ['https://thunderbird.asu.edu/']
    start_urls = ['http://https://thunderbird.asu.edu//']

    def parse(self, response):
        pass
