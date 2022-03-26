import scrapy


class Ind0031Spider(scrapy.Spider):
    name = 'ind_0031'
    allowed_domains = ['https://www.mdi.ac.in/']
    start_urls = ['http://https://www.mdi.ac.in//']

    def parse(self, response):
        pass
