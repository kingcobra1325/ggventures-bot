import scrapy


class Ind0018Spider(scrapy.Spider):
    name = 'ind_0018'
    allowed_domains = ['https://www.iitb.ac.in/']
    start_urls = ['http://https://www.iitb.ac.in//']

    def parse(self, response):
        pass
