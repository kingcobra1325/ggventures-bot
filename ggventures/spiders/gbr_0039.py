import scrapy


class Gbr0039Spider(scrapy.Spider):
    name = 'gbr_0039'
    allowed_domains = ['https://www.ncl.ac.uk/business/']
    start_urls = ['http://https://www.ncl.ac.uk/business//']

    def parse(self, response):
        pass
