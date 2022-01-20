import scrapy


class Usa0126Spider(scrapy.Spider):
    name = 'usa_0126'
    allowed_domains = ['https://www.unlv.edu/business']
    start_urls = ['http://https://www.unlv.edu/business/']

    def parse(self, response):
        pass
