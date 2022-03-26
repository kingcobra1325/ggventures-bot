import scrapy


class Ind0011Spider(scrapy.Spider):
    name = 'ind_0011'
    allowed_domains = ['https://www.iift.ac.in/']
    start_urls = ['http://https://www.iift.ac.in//']

    def parse(self, response):
        pass
