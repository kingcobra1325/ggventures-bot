import scrapy


class Ind0012Spider(scrapy.Spider):
    name = 'ind_0012'
    allowed_domains = ['https://www.iima.ac.in/']
    start_urls = ['http://https://www.iima.ac.in//']

    def parse(self, response):
        pass
