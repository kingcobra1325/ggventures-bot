import scrapy


class Usa0005Spider(scrapy.Spider):
    name = 'usa-0005'
    allowed_domains = ['https://zicklin.baruch.cuny.edu/']
    start_urls = ['http://https://zicklin.baruch.cuny.edu//']

    def parse(self, response):
        pass
