import scrapy


class Usa0121Spider(scrapy.Spider):
    name = 'usa_0121'
    allowed_domains = ['https://herbert.miami.edu/']
    start_urls = ['http://https://herbert.miami.edu//']

    def parse(self, response):
        pass
