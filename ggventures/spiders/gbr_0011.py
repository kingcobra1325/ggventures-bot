import scrapy


class Gbr0011Spider(scrapy.Spider):
    name = 'gbr_0011'
    allowed_domains = ['https://www.henley.ac.uk/']
    start_urls = ['http://https://www.henley.ac.uk//']

    def parse(self, response):
        pass
