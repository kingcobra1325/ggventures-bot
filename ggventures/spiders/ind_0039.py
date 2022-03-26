import scrapy


class Ind0039Spider(scrapy.Spider):
    name = 'ind_0039'
    allowed_domains = ['https://www.spjain.org/']
    start_urls = ['http://https://www.spjain.org//']

    def parse(self, response):
        pass
