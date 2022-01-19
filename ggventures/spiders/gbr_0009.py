import scrapy


class Gbr0009Spider(scrapy.Spider):
    name = 'gbr_0009'
    allowed_domains = ['https://www.cranfield.ac.uk/som']
    start_urls = ['http://https://www.cranfield.ac.uk/som/']

    def parse(self, response):
        pass
