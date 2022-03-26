import scrapy


class Ind0049Spider(scrapy.Spider):
    name = 'ind_0049'
    allowed_domains = ['https://ximb.edu.in/']
    start_urls = ['http://https://ximb.edu.in//']

    def parse(self, response):
        pass
