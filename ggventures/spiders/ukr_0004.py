import scrapy


class Ukr0004Spider(scrapy.Spider):
    name = 'ukr_0004'
    allowed_domains = ['https://kmbs.ua/en/']
    start_urls = ['http://https://kmbs.ua/en//']

    def parse(self, response):
        pass
