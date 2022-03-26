import scrapy


class Ind0023Spider(scrapy.Spider):
    name = 'ind_0023'
    allowed_domains = ['https://cit.edu/']
    start_urls = ['http://https://cit.edu//']

    def parse(self, response):
        pass
