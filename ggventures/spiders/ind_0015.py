import scrapy


class Ind0015Spider(scrapy.Spider):
    name = 'ind_0015'
    allowed_domains = ['https://www.iimidr.ac.in/']
    start_urls = ['http://https://www.iimidr.ac.in//']

    def parse(self, response):
        pass
