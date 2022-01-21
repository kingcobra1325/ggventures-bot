import scrapy


class Usa0146Spider(scrapy.Spider):
    name = 'usa_0146'
    allowed_domains = ['https://www1.villanova.edu/university/business.html']
    start_urls = ['http://https://www1.villanova.edu/university/business.html/']

    def parse(self, response):
        pass
