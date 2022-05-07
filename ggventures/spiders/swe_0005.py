import scrapy


class Swe0005Spider(scrapy.Spider):
    name = 'swe_0005'
    allowed_domains = ['https://www.hhs.se/']
    start_urls = ['http://https://www.hhs.se//']

    def parse(self, response):
        pass
