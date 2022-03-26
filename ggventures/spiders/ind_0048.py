import scrapy


class Ind0048Spider(scrapy.Spider):
    name = 'ind_0048'
    allowed_domains = ['https://ximb.edu.in/']
    start_urls = ['http://https://ximb.edu.in//']

    def parse(self, response):
        pass
