import scrapy


class Ind0046Spider(scrapy.Spider):
    name = 'ind_0046'
    allowed_domains = ['https://www.ubs.puchd.ac.in/']
    start_urls = ['http://https://www.ubs.puchd.ac.in//']

    def parse(self, response):
        pass
