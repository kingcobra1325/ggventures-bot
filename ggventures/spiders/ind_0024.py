import scrapy


class Ind0024Spider(scrapy.Spider):
    name = 'ind_0024'
    allowed_domains = ['https://www.imt.edu/']
    start_urls = ['http://https://www.imt.edu//']

    def parse(self, response):
        pass
