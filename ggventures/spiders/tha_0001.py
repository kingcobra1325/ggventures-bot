import scrapy


class Tha0001Spider(scrapy.Spider):
    name = 'tha_0001'
    allowed_domains = ['https://www.som.ait.ac.th/']
    start_urls = ['http://https://www.som.ait.ac.th//']

    def parse(self, response):
        pass
