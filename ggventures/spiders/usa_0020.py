import scrapy


class Usa0020Spider(scrapy.Spider):
    name = 'usa_0020'
    allowed_domains = ['https://www.johnson.cornell.edu/']
    start_urls = ['http://https://www.johnson.cornell.edu//']

    def parse(self, response):
        pass
