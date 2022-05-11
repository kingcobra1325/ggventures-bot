import scrapy


class Ukr0003Spider(scrapy.Spider):
    name = 'ukr_0003'
    allowed_domains = ['https://kneu.edu.ua/en/']
    start_urls = ['http://https://kneu.edu.ua/en//']

    def parse(self, response):
        pass
