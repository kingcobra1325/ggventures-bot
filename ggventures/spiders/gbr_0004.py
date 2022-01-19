import scrapy


class Gbr0004Spider(scrapy.Spider):
    name = 'gbr_0004'
    allowed_domains = ['https://www.bradford.ac.uk/management/']
    start_urls = ['http://https://www.bradford.ac.uk/management//']

    def parse(self, response):
        pass
