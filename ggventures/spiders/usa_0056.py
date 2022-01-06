import scrapy


class Usa0056Spider(scrapy.Spider):
    name = 'usa_0056'
    allowed_domains = ['https://bschool.pepperdine.edu/']
    start_urls = ['http://https://bschool.pepperdine.edu//']

    def parse(self, response):
        pass
