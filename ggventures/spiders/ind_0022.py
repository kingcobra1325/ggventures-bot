import scrapy


class Ind0022Spider(scrapy.Spider):
    name = 'ind_0022'
    allowed_domains = ['https://www.iilm.edu/']
    start_urls = ['http://https://www.iilm.edu//']

    def parse(self, response):
        pass
