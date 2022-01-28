import scrapy


class Gbr0038Spider(scrapy.Spider):
    name = 'gbr_0038'
    allowed_domains = ['https://business.leeds.ac.uk/']
    start_urls = ['http://https://business.leeds.ac.uk//']

    def parse(self, response):
        pass
