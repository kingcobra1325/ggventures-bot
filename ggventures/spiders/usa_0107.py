import scrapy


class Usa0107Spider(scrapy.Spider):
    name = 'usa_0107'
    allowed_domains = ['https://www.colorado.edu/business/']
    start_urls = ['http://https://www.colorado.edu/business//']

    def parse(self, response):
        pass
