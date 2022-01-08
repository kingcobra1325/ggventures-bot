import scrapy


class Usa0071Spider(scrapy.Spider):
    name = 'usa_0071'
    allowed_domains = ['https://www.suffolk.edu/business']
    start_urls = ['http://https://www.suffolk.edu/business/']

    def parse(self, response):
        pass
