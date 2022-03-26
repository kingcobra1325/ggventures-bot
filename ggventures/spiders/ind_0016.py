import scrapy


class Ind0016Spider(scrapy.Spider):
    name = 'ind_0016'
    allowed_domains = ['https://www.iimk.ac.in/']
    start_urls = ['http://https://www.iimk.ac.in//']

    def parse(self, response):
        pass
