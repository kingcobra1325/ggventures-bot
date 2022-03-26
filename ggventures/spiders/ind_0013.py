import scrapy


class Ind0013Spider(scrapy.Spider):
    name = 'ind_0013'
    allowed_domains = ['https://www.iimb.ac.in/home']
    start_urls = ['http://https://www.iimb.ac.in/home/']

    def parse(self, response):
        pass
