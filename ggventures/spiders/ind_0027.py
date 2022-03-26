import scrapy


class Ind0027Spider(scrapy.Spider):
    name = 'ind_0027'
    allowed_domains = ['https://jbims.edu/']
    start_urls = ['http://https://jbims.edu//']

    def parse(self, response):
        pass
