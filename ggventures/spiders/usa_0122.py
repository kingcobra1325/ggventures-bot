import scrapy


class Usa0122Spider(scrapy.Spider):
    name = 'usa_0122'
    allowed_domains = ['https://carlsonschool.umn.edu/']
    start_urls = ['http://https://carlsonschool.umn.edu//']

    def parse(self, response):
        pass
