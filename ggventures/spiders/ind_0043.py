import scrapy


class Ind0043Spider(scrapy.Spider):
    name = 'ind_0043'
    allowed_domains = ['https://www.tapmi.edu.in/']
    start_urls = ['http://https://www.tapmi.edu.in//']

    def parse(self, response):
        pass
