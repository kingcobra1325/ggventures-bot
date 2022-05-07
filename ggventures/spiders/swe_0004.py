import scrapy


class Swe0004Spider(scrapy.Spider):
    name = 'swe_0004'
    allowed_domains = ['https://www.lusem.lu.se/']
    start_urls = ['http://https://www.lusem.lu.se//']

    def parse(self, response):
        pass
