import scrapy


class Ind0040Spider(scrapy.Spider):
    name = 'ind_0040'
    allowed_domains = ['https://www.siescoms.edu.in/']
    start_urls = ['http://https://www.siescoms.edu.in//']

    def parse(self, response):
        pass
