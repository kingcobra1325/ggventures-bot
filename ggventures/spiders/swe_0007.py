import scrapy


class Swe0007Spider(scrapy.Spider):
    name = 'swe_0007'
    allowed_domains = ['https://www.umu.se/en/usbe/']
    start_urls = ['http://https://www.umu.se/en/usbe//']

    def parse(self, response):
        pass
