import scrapy


class Ind0033Spider(scrapy.Spider):
    name = 'ind_0033'
    allowed_domains = ['https://www.nitie.ac.in/']
    start_urls = ['http://https://www.nitie.ac.in//']

    def parse(self, response):
        pass
