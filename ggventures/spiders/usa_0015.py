import scrapy


class Usa0015Spider(scrapy.Spider):
    name = 'usa_0015'
    allowed_domains = ['https://weatherhead.case.edu/']
    start_urls = ['http://https://weatherhead.case.edu//']

    def parse(self, response):
        pass
