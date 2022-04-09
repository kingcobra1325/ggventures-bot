import scrapy


class Ita0015Spider(scrapy.Spider):
    name = 'ita_0015'
    allowed_domains = ['https://www.economia.unifi.it/']
    start_urls = ['http://https://www.economia.unifi.it//']

    def parse(self, response):
        pass
