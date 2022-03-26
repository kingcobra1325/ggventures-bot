import scrapy


class Ind0017Spider(scrapy.Spider):
    name = 'ind_0017'
    allowed_domains = ['https://www.iiml.ac.in/']
    start_urls = ['http://https://www.iiml.ac.in//']

    def parse(self, response):
        pass
