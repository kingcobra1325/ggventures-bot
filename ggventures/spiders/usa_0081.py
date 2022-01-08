import scrapy


class Usa0081Spider(scrapy.Spider):
    name = 'usa_0081'
    allowed_domains = ['https://www.memphis.edu/fcbe/']
    start_urls = ['http://https://www.memphis.edu/fcbe//']

    def parse(self, response):
        pass
