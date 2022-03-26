import scrapy


class Ind0038Spider(scrapy.Spider):
    name = 'ind_0038'
    allowed_domains = ['https://www.psgim.ac.in/']
    start_urls = ['http://https://www.psgim.ac.in//']

    def parse(self, response):
        pass
