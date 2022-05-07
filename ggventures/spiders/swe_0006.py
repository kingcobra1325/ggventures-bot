import scrapy


class Swe0006Spider(scrapy.Spider):
    name = 'swe_0006'
    allowed_domains = ['https://www.su.se/stockholm-business-school/']
    start_urls = ['http://https://www.su.se/stockholm-business-school//']

    def parse(self, response):
        pass
