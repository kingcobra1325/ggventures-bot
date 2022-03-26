import scrapy


class Ind0050Spider(scrapy.Spider):
    name = 'ind_0050'
    allowed_domains = ['https://www.xlri.ac.in/']
    start_urls = ['http://https://www.xlri.ac.in//']

    def parse(self, response):
        pass
