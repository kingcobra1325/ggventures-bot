import scrapy


class Phl0005Spider(scrapy.Spider):
    name = 'phl_0005'
    allowed_domains = ['http://graduateschool.ust.edu.ph/']
    start_urls = ['http://http://graduateschool.ust.edu.ph//']

    def parse(self, response):
        pass
