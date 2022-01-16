import scrapy


class Usa0140Spider(scrapy.Spider):
    name = 'usa_0140'
    allowed_domains = ['https://www.uvm.edu/business']
    start_urls = ['http://https://www.uvm.edu/business/']

    def parse(self, response):
        pass
