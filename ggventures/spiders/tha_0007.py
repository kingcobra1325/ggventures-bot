import scrapy


class Tha0007Spider(scrapy.Spider):
    name = 'tha_0007'
    allowed_domains = ['https://tu.ac.th/en']
    start_urls = ['http://https://tu.ac.th/en/']

    def parse(self, response):
        pass
