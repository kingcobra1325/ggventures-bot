import scrapy


class Swe0003Spider(scrapy.Spider):
    name = 'swe_0003'
    allowed_domains = ['https://liu.se/en/organisation/liu/iei/fek']
    start_urls = ['http://https://liu.se/en/organisation/liu/iei/fek/']

    def parse(self, response):
        pass
