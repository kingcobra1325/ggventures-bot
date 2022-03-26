import scrapy


class Ind0014Spider(scrapy.Spider):
    name = 'ind_0014'
    allowed_domains = ['https://www.iimcal.ac.in/']
    start_urls = ['http://https://www.iimcal.ac.in//']

    def parse(self, response):
        pass
