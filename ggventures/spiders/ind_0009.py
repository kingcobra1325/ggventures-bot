import scrapy


class Ind0009Spider(scrapy.Spider):
    name = 'ind_0009'
    allowed_domains = ['https://gim.ac.in/']
    start_urls = ['http://https://gim.ac.in//']

    def parse(self, response):
        pass
