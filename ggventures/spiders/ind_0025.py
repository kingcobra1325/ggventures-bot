import scrapy


class Ind0025Spider(scrapy.Spider):
    name = 'ind_0025'
    allowed_domains = ['https://www.irma.ac.in/']
    start_urls = ['http://https://www.irma.ac.in//']

    def parse(self, response):
        pass
