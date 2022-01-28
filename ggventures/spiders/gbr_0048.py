import scrapy


class Gbr0048Spider(scrapy.Spider):
    name = 'gbr_0048'
    allowed_domains = ['https://www.aber.ac.uk/en/abs/']
    start_urls = ['http://https://www.aber.ac.uk/en/abs//']

    def parse(self, response):
        pass
