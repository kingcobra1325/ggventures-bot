import scrapy


class Usa0010Spider(scrapy.Spider):
    name = 'usa-0010'
    allowed_domains = ['https://www.bradley.edu/academic/colleges/fcba/']
    start_urls = ['http://https://www.bradley.edu/academic/colleges/fcba//']

    def parse(self, response):
        pass
