import scrapy


class Usa0084Spider(scrapy.Spider):
    name = 'usa_0084'
    allowed_domains = ['https://www.mgt.unm.edu/']
    start_urls = ['http://https://www.mgt.unm.edu//']

    def parse(self, response):
        pass
